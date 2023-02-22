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
    Usuario = user["id"]

    info = db.getUser(Usuario)
    profe = info["nombre"] #poner "user"
    id = db.getLastId("Tareas")
    
    tarea = {
    "id" : id ,
    "profesor": profe,
    "cuerpo": asignacion, 
    "titulo": titulo
}        
    return json.dumps(tarea)


def subirTarea(datos:str,n_tarea:int):

     Usuario = user["id"]




