from pymongo import MongoClient
import urllib.parse
from src.components.colegio import *
from src.components.users import *
import json

arr_clas:list[Clase] = []



    

def buscar_clase_clave(clave:str) -> Clase:
    for clase in arr_clas:
        if clase.Clave() == clave:
            return clase
    return None

def buscar_clase_profe(profe:str) -> Clase:
    if arr_clas != None:
        for clase in arr_clas:
            if clase.Profesor() == profe:
                return clase
        return None

def hechar_de_clase(profe:str, usuario:str) -> None:
    clase:Clase = buscar_clase_profe(profe)
    clase.Alumnos().remove(usuario)
    clase.Imagenes().remove(usuario)
    return 'Eliminado'
            
