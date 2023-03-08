import datetime
import json

class Asignatura:

    nombre: str
    horasSemanales: int

    def __init__(self, nombre:str=None, horasSemanales:int=None) -> None:
        self.nombre = nombre
        self.horasSemanales = horasSemanales

    def toJson(self) -> dict:
        json = {
            "nombre":self.nombre,
            "horasSemanales":self.horasSemanales
        }
        return json



class Profesor:
    
    id: int
    nombre: str
    tutor: bool
    horario:list[list[str]]
    asignaturas: list[Asignatura]

    def __init__(self, id, tutor:bool=None, nombre:str=None, horario:list[list[str]]=None, asignaturas:list[Asignatura]=None):
        self.id = id
        self.tutor = tutor
        self.nombre = nombre
        self.horario = horario
        self.asignaturas = asignaturas
    
    def toJson(self) -> dict:        
        json = {
            "nombre":self.nombre,
            "tutor":self.tutor,
            "horario": self.horario,
            "asignaturas":self.asignaturas
        }
        return json

class Grupo:

    nombre: str
    asignaturas: list[Asignatura]
    tutor: Profesor
    profesores: list[Profesor]
    horario: str

    def __init__(self, nombre:str=None, asignaturas:list[Asignatura]=None, tutor:Profesor=None, profesores:list[Profesor]=None, horario:str=None) -> None:
        self.nombre = nombre
        self.asignaturas = asignaturas
        self.tutor = tutor
        self.profesores = profesores
        self.horario = horario



class Hora_horario:
    nombre: Asignatura
    tiempo:datetime.datetime
    grupo: Grupo
    profesor: Profesor

    def __init__(self, nombre:Asignatura=None, tiempo:datetime.datetime=None, grupo:Grupo=None, profesor:Profesor=None) -> None:
        self.nombre = nombre
        self.tiempo = tiempo
        self.grupo = grupo
        self.profesor = profesor
    
    def toJson(self) -> str:
        return json.dumps({
            "nombre":self.nombre.nombre,
            "tiempo":self.tiempo,
            "grupo":self.grupo.nombre,
            "profesor":self.profesor.nombre
        }, default=str)
    

class Tarea:
    titulo:str
    tarea:str
    tiempo:datetime.datetime
    profesor: Profesor


    def __init__(self, titulo:str,tarea:str,tiempo:datetime.datetime, profesor:Profesor):
        self.titulo = titulo
        self.tarea = tarea
        self.tiempo = tiempo
        self.profesor = profesor

    def toJson(self) -> str:
        return json.dumps({
            "titulo":self.titulo,
            "tiempo":self.tiempo,
            "profesor":self.profesor.nombre,
            "tarea":self.tarea
        }, default=str)

    
class dia:
    horario: list[Hora_horario] 
    dia_semana: str
    grupo: Grupo

    def __init__(self, horario:list[Hora_horario]=None, dia_semana:str=None, grupo:Grupo=None) -> None:
        self.horario = horario
        self.dia_semana = dia_semana
        self.grupo = grupo


class semana:
    horario: list[dia]
    grupo: Grupo

    def __init__(self, horario:list[dia]=None, grupo:Grupo=None) -> None:
        self.horario = horario
        self.grupo = grupo

    

