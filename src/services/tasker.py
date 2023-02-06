from src.components.colegio import *
from src.components.users import *



def __init__(self) -> None:
        pass
    
    
    
# --------------------------------------------------------------------------------------------
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
# ----------------------------------------------------------------------------------------


 # profesores publican tareas
def crearTarea():
    
    
    
    return 


# alumno sube respuesta de la tarea
def subirTarea():
    
    
    
    
    return



#profesores eliminan tareas
def eliminarTarea():
    return

# imprime Tarea
def imprimeTarea():
    return




