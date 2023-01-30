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
        for item in coll.find({}):
            list.append(item)
        return list
    
    def getUser(self, id:int) -> list[dict]:
        coll = self.database["Usuarios"]
        for item in coll.find({"id":id}):
            return item
    
    def insertUser(self, usuario:dict):
        ids = []
        for user in self.listUsers():
            ids.append(user["id"])
        usuario["id"] = max(ids)+1
        coll = self.database["Usuarios"]
        coll.insert_one(usuario)
    
    def uploadHorario(self, listado:list[dict]):
        pass
    
    