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
    
    def listUsers(self) -> list:
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
    
    def insertUser(self, usuario:Usuario):
        insertDict = usuario.toJson()
        for user in self.listUsers():
            if user["id"] == insertDict["id"]:
                return "Not a valid id"
        coll = self.database["Usuarios"]
        coll.insert_one(insertDict)
    
    def uploadHorario(self, listado:list[dict]):
        pass
    
    