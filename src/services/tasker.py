from src.components.colegio import *
from src.components.users import *
import json 
import datetime







def __init__(self) -> None:
    pass





 # profesores publican tareas
def crearTarea(datos:str,):
 
    titulo = datos["titulo"]
    asignacion = datos["tarea"]
    
    hora_actual = datetime.datetime.now()
    # busca quien inicio secion (profesor)
    # profe =  tengo que pillara el json que me da edu en appliation
    
    tarea = json.loads({
    "profesor": profe,
    "tiempo": hora_actual,
    "cuerpo": asignacion, 
    "titulo": titulo
})
    return json.loads(tarea)


# alumno sube respuesta de la tarea
def subirTarea():
    
    
    
    
    return



#profesores eliminan tareas
def eliminarTarea():
    return

# imprime Tarea
def imprimeTarea():
    return




