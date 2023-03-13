from pymongo import MongoClient
import urllib.parse
from src.components.colegio import *
from src.components.users import *
import json

arr_clas:list[Clase] = []


def crear_clase(clave:str, profe:str, alumnos:list[str]) -> Clase:
    newclase:Clase = Clase()
    newclase.clave = clave
    newclase.profesor = profe
    newclase.alumnos = alumnos
    checks = []
    for alumno in newclase.alumnos:
        checks.append(0)
    newclase.Checked(checks)
    arr_clas.append(newclase)
    return newclase

def buscar_clase_clave(clave:str) -> Clase:
    for clase in arr_clas:
        if clase.clave == clave:
            return clase
    return None

def buscar_clase_profe(profe:str) -> Clase:
    if arr_clas != None:
        for clase in arr_clas:
            if clase.profesor == profe:
                return clase
        return None

def hechar_de_clase(profe:str, usuario:str) -> None:
    clase:Clase = buscar_clase_profe(profe)
    clase.alumnos.remove(usuario)
    return 'Eliminado'
            
