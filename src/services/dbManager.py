from pymongo import MongoClient
import urllib.parse
from src.components.colegio import *
from src.components.users import *
import json



class DbManager:
    """
        Clase para controlar la base de datos
        
        Funciones:
        ---------
         - listAnime()
         - listUsers()
    """
    
    CONNECTION_STRING = f"mongodb+srv://admin:"+urllib.parse.quote("Joyfe@2023")+"@python.0rrjnq0.mongodb.net/?retryWrites=true&w=majority"
    client = MongoClient(CONNECTION_STRING)
    database = client["Python"]
    
    
    
    def __init__(self) -> None:
        pass
    
    def listUsers(self) -> list[dict]:
        """
            Lista Los usuarios de la base de datos
        """
        coll = self.database["Usuarios"]
        list = []
        for item in coll.find({},{"_id":0}):
            list.append(item)
        return list
    
    def listTareas(self) -> list[dict]:
        coll = self.database["Tareas"]
        list = []
        for item in coll.find({},{"_id":0}):
            list.append(item)
        return list
        
    
    def getUser(self, id:int) -> dict:
        coll = self.database["Usuarios"]
        for item in coll.find({"id":id}):
            return item
    
    def insertUser(self, usuario:Usuario):
        insertDict = usuario.toJson()
        for user in self.listUsers():
            if user["id"] == insertDict["id"]:
                return "Not a valid id"
        coll = self.database["Usuarios"]
        coll.insert_one(insertDict)
        return "donete"
        
    
    def insertTarea(self, tarea:Tarea):
        insertDict = json.loads(tarea)
        njlk =  self.listTareas()
        for tarea in njlk:
            if tarea["id"] == insertDict["id"]:
                return "Not a valid id"
        coll = self.database["Tareas"]
        coll.insert_one(insertDict)
        
        
    #revisar por edu
    def getLastId(self,nombre:str):
        coll = self.database[nombre]
        last_id = coll.find({},{"_id":0, "id":1}).sort("id", -1).limit(1)
        for id in last_id:
            print(id["id"] + 1 ) 
        return id["id"] + 1 
        
    def uploadHorario(self, listado:list[dict]):
        pass
    
    def getTareas(self, gmail:str) -> list[dict]:
        tareas:Tarea = []
        for tarea in self.listTareas():
            if gmail in tarea['Alumnos']:
                tareas.append(tarea)
        return tareas
    
    def getGrupos(self) ->list[str]:
        call = self.database["Grupos"]
        grupos:list[str] = []
        for grup in call.find({}):
            grupos.append(grup["nombre"])
        return grupos
    
    def getAlumnos(self, grupo) -> list[str]:
        call = self.database["Grupos"]
        jamon = call.find_one({"nombre":grupo})["alumnos"]
        return jamon
            
    
