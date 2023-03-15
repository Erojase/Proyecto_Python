from pymongo import MongoClient
import urllib.parse
from src.components.colegio import *
from src.components.users import *
from datetime import datetime
from bson import ObjectId
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
        db = self.database["Usuarios"]
        insertDict = usuario.toJson()
        db.insert_one(insertDict)
        return "User successfully registered"
        
    
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
        projection = {"_id":0}
        for grup in db.find(filter,projection):
            grupos.append(grup["nombre"])
        return grupos
    
    def getAlumnos(self, grupo) -> list[str]:
        db = self.database["Grupos"]
        
        filter = {"nombre":grupo}
        projection = {"_id":0,"alumnos":1}
        return db.find_one(filter,projection) # devuelve un array de alumnos, por eso el find_one
            
    def historicoCrear(self, alumnos:list[str], profesor:str):
        db = self.database['Historico']
        horas_conexion = []
        for al in alumnos:
            horas_conexion.append(None)
        return db.insert_one({'Alumnos': alumnos, 'Hora_creacion': datetime.now().strftime("%d/%m/%Y %H:%M:%S"), 'Hora_conexion_alumno': horas_conexion}).inserted_id
        
        
    def crearClase(self, alumnos:list[str], profesor:str, clave:str):
        db = self.database['Clases']
        checks:list[int] = []
        for al in alumnos:
            checks.append(0)
        return db.insert_one({'Alumnos': alumnos, 'Profesor': profesor, 'Clave': clave, 'Checks': checks}).inserted_id
    
    def buscarClaseClave(self, clave:str, al:str):
        db = self.database['Clases']
        filter = {"Clave":clave}
        row = db.find_one(filter)
        cont:int = 0
        for alumno in row['Alumnos']:
            if alumno == al:
                row['Checks'][cont] = 1
            cont += 1
        checks = row["Checks"]
        newvalues = {"$set": {'Checks':checks}}
        db.update_one(filter, newvalues)
        return 'Checkeado'

    def buscarClaseProfe(self, profe:str, objectId:str):
        db = self.database['Clases']
        filter = {"Profesor":profe}
        projection = {"_id":0,"Checks":1}
        row = db.find_one(filter, projection)
        db = self.database['Historico']
        oid = ObjectId()
        filter = {"_id": ObjectId(objectId)}
        hrow = db.find_one(filter)
        # for r in hrow['Hora_conexion_alumno']:
            
        return row

    def getProfesores(self) ->list[str]:
        db = self.database["Usuarios"]
        grupos:list[str] = []
        
        filter = {"tipo":Tipo.Profesor.name}
        projection = {"_id":0}
        for grup in db.find(filter,projection):
            grupos.append(grup["nick"])
        return grupos
    
    def getAsignaturas(self) ->list[str]:
        db = self.database["Asignaturas"]
        grupos:list[str] = []
        
        filter = {}
        projection = {"_id":0}
        for grup in db.find(filter,projection):
            grupos.append(grup["nombre"])
        return grupos
    
    
    def crearGrupo(self, grupo:Grupo):
        db = self.database["Grupos"]
        return str(db.insert_one( grupo.toJson()).inserted_id)
    
    
    
    # #######################################    Bot
        
    def listUsersNick(self) -> list[dict]:
        """
            Lista Los usuarios de la base de datos
        """
        db = self.database["Usuarios"]
        list = []
        
        filter = {}
        projection = {"nick":1}       
        for item in db.find(filter,projection):
            list.append(item)
        return list
    
    def listOneUserStats(self, user:str) -> list[dict]:
        """
            Lista Los usuarios de la base de datos
        """
        db = self.database["Usuarios"]
        list = []
        
        filter = {"nick":user}
        projection = {"_id":0}       
        for item in db.find(filter,projection):
            list.append(item)
        return list
        
    def listGruposName(self) ->list[str]:
        db = self.database["Grupos"]
        grupos:list[str] = []
        
        filter = {}
        projection = {"nombre":1}
        for grup in db.find(filter,projection):
            grupos.append(grup)
        return grupos
    
    def listAsignaturasName(self) ->list[str]:
        db = self.database["Asignaturas"]
        grupos:list[str] = []
        
        filter = {}
        projection = {"nombre":1}
        for grup in db.find(filter,projection):
            grupos.append(grup)
        return grupos