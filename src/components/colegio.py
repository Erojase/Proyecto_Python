import datetime
import json



class Asignatura:

    _nombre: str
    _horasSemanales: int

    def __init__(self, nombre:str=None, horasSemanales:int=None) -> None:
        self._nombre = nombre
        self._horasSemanales = horasSemanales
        pass

    def Nombre(self, value:str=None):
        if value != None:
            self._nombre = value 
        return self._nombre

    def HorasSemanales(self, value:int=None):
        if value != None:
            self._horasSemanales = value 
        return self._horasSemanales

    def ToJson(self) -> dict:
        json = {
            "nombre":self._nombre,
            "horasSemanales":self._horasSemanales
        }
        return json



class Profesor:
    
    _id: int
    _nombre: str
    _tutor: bool
    _horario:list[list[str]]
    _asignaturas: list[Asignatura]

    def __init__(self, id, tutor:bool=None, nombre:str=None, horario:list[list[str]]=None, asignaturas:list[Asignatura]=None):
        self._id = id
        self._tutor = tutor
        self._nombre = nombre
        self._horario = horario
        self._asignaturas = asignaturas

    def Id(self, value:str=None):
        return self._id

    def Nombre(self, value:str=None):
        if value != None:
            self._nombre = value 
        return self._nombre
    
    def Tutor(self, value:bool=None):
        if value != None:
            self._tutor = value 
        return self._tutor
    
    def Horario(self, value:list[list[str]]=None):
        if value != None:
            self._horario = value 
        return self._horario
    
    def Asignaturas(self, value:list[Asignatura]=None):
        if value != None:
            self._asignaturas = value 
        return self._asignaturas

    def ToJson(self) -> dict:
        asignatura_list = ""
        for asign in self._asignaturas:
            asignatura_list += asign.Nombre()+","
        
        json = {
            "nombre":self._nombre,
            "tutor":self._tutor,
            "horario":{
                        "inicio":self._horario[0][0],
                        "fin":self._horario[0][1]
                        },
            "asignaturas":asignatura_list
        }
        return json


class Grupo:

    _nombre: str
    _asignaturas: list[Asignatura]
    _tutor: Profesor
    _profesores: list[Profesor]
    _horario: str

    def __init__(self, nombre:str=None, asignaturas:list[Asignatura]=None, tutor:Profesor=None, profesores:list[Profesor]=None, horario:str=None) -> None:
        self._nombre = nombre
        self._asignaturas = asignaturas
        self._tutor = tutor
        self._profesores = profesores
        self._horario = horario
        pass


    def Nombre(self, value:str=None):
        if value != None:
            self._nombre = value 
        return self._nombre

    def Asignaturas(self, value:list[Asignatura]=None):
        if value != None:
            self._asignaturas = value 
        return self._asignaturas


    def Tutor(self, value:Profesor=None):
        if value != None:
            self._tutor = value 
        return self._tutor


    def Profesores(self, value:list[Profesor]=None):
        if value != None:
            self._profesores = value 
        return self._profesores

    def Horario(self, value:str=None):
        if value != None:
            self._horario = value 
        return self._horario


class Hora_horario:
    _nombre: Asignatura
    _tiempo:datetime.datetime
    _grupo: Grupo
    _profesor: Profesor

    def __init__(self, nombre:Asignatura=None, tiempo:datetime.datetime=None, grupo:Grupo=None, profesor:Profesor=None) -> None:
        self._nombre = nombre
        self._tiempo = tiempo
        self._grupo = grupo
        self._profesor = profesor
        pass

    def Nombre(self, value:Asignatura=None):
        if value != None:
            self._nombre = value 
        return self._nombre

    def Tiempo(self, value:datetime.datetime=None):
        if value != None:
            self._tiempo = value 
        return self._tiempo

    def Grupo(self, value:Grupo=None):
        if value != None:
            self._grupo = value 
        return self._grupo

    def Profesor(self, value:Profesor=None):
        if value != None:
            self._profesor = value 
        return self._profesor
    
    
    def toJson(self) -> str:
        return json.dumps({
            "nombre":self._nombre.Nombre(),
            "tiempo":self._tiempo,
            "grupo":self._grupo.Nombre(),
            "profesor":self._profesor.Nombre()
        }, default=str)
    

class Tarea:
    _nombre: str
    _tiempo:datetime.datetime
    _profesor: Profesor


    def __init__(self, Nombre:str, tiempo:datetime.datetime, profesor:Profesor):
        pass
    
    def Nombre(self, value:str=None):
        if value != None:
            self._nombre = value
        return self._nombre


    def Tiempo(self, value:datetime.datetime=None):
            if value != None:
                self._tiempo = value 
            return self._tiempo


    def Profesor(self, value:Profesor=None):
        if value != None:
            self._profesor = value 
        return self._profesor


    def toJson(self) -> str:
        return json.dumps({
            "nombre":str,
            "tiempo":self._tiempo,
            "profesor":self._profesor.Nombre()
        }, default=str)

    
class dia:
    _horario: list[Hora_horario] 
    _dia_semana: str
    _grupo: Grupo

    def __init__(self, horario:list[Hora_horario]=None, dia_semana:str=None, grupo:Grupo=None) -> None:
        self._horario = horario
        self._dia_semana = dia_semana
        self._grupo = grupo

    def Horario(self, value:list[Hora_horario]=None):
        if value != None:
            self._horario = value
        return self._horario

    def DiaSemana(self, value:str=None):
        if value != None:
            self._dia_semana = value
        return self._dia_semana

    def Grupo(self, value:Grupo=None):
        if value != None:
            self._grupo = value 
        return self._grupo


class semana:
    _horario: list[dia]
    _grupo: Grupo

    def __init__(self, horario:list[dia]=None, grupo:Grupo=None) -> None:
        self._horario = horario
        self._grupo = grupo

    def Horario(self, value:list[dia]=None):
        if value != None:
            self._horario = value
        return self._horario

    def Grupo(self, value:Grupo=None):
        if value != None:
            self._grupo = value 
        return self._grupo

    

