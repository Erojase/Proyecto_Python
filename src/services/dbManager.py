from pymongo import MongoClient
import urllib.parse
from src.components.colegio import *
from src.components.users import *
from datetime import datetime
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
        db = self.database["Usuarios"]
        list = []
        
        filter = {}
        projection = {"_id":0}       
        for item in db.find(filter,projection):
            list.append(item)
        return list
    
    def getOneUser(self, filter:dict, projection):
        db = self.database["Usuarios"]
        return db.find_one(filter,projection)
    
    def listTareas(self) -> list[dict]:
        db = self.database["Tareas"]
        list = []
        
        filter = {}
        projection = {"_id":0}       
        for item in db.find(filter,projection):
            list.append(item)
        return list
        
    
    def getUser(self, id:int) -> dict:
        db = self.database["Usuarios"]
        
        filter = {"id":id}
        projection = {}       
        for item in db.find(filter,projection):
            return item
    
    def insertUser(self, usuario:Usuario):
        insertDict = usuario.toJson()
        for user in self.listUsers():
            if user["id"] == insertDict["id"]:
                return "Not a valid id"
        db = self.database["Usuarios"]
        db.insert_one(insertDict)
        return "donete"
        
    
    def insertTarea(self, tarea:Tarea):
        insertDict = json.loads(tarea)
        njlk =  self.listTareas()
        for tarea in njlk:
            if tarea["id"] == insertDict["id"]:
                return "Not a valid id"
        db = self.database["Tareas"]
        db.insert_one(insertDict) 
    
    
    def getGrupos(self) ->list[str]:
        db = self.database["Grupos"]
        grupos:list[str] = []
        
        filter = {}
        projection = {}
        for grup in db.find(filter,projection):
            grupos.append(grup["nombre"])
        return grupos
    
    def getAlumnos(self, grupo) -> list[str]:
        db = self.database["Grupos"]
        
        filter = {"nombre":grupo}
        projection = {"alumnos":1}
        return db.find_one(filter,projection)
            
    def historicoCrear(self, alumnos:list[str], profesor:str):
        db = self.database['Historico']
        horas_conexion = []
        for al in alumnos:
            horas_conexion.append(None)
        return db.insert_one({'Alumnos': alumnos, 'Hora_creacion': datetime.now().strftime("%d/%m/%Y %H:%M:%S"), 'Hora_conexion_alumno': horas_conexion})
        
        
    
