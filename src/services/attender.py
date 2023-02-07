from pymongo import MongoClient
import urllib.parse
from src.components.colegio import *
from src.components.users import *
import json

arr_clas:list[Clase] = []

def buscar_clase(clave:str) -> Clase:
    for clase in arr_clas:
        if clase.Clave() == clave:
            return clase