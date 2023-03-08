from src.components.colegio import *
from src.components.users import *
from src.services.dbManager import DbManager
import json 
import datetime

db = DbManager()



 # profesores publican tareas
def crearTarea(datos:str,user:str,):
    titulo = datos["titulo"]
    asignacion = datos["tarea"]
    Usuario = user["nick"]

    
    # profe = info["nombre"] #poner "user"
    # id = db.getLastId("Tareas")
    
    tarea = {
        "Alumnos": DbManager.getAlumnos(datos['grupo']),
        "Profesor": Usuario,
        "Descripcion": asignacion, 
        "Titulo": titulo
    }        
    return json.dumps(tarea)


def subirTarea(datos:str,n_tarea:int):
    pass
    #  Usuario = user["id"]




