from enum import Enum
import os
from src.components.colegio import *

class Tipo(Enum):
    Alumno = 0
    Profesor = 1

class Usuario:
    
    _id:int
    _nick:str
    _nombre:str
    _apellido:str
    _passwd:str
    _mail:str
    _tipo:Tipo
    
    _profesor:Profesor | None 
    
    def __init__(self, id:int, nick:str, nombre:str, apellido:str, passwd:str, mail:str, tipo:Tipo, profesor:Profesor | None = None) -> dict:
        self._id = id
        self._nick = nick
        self._nombre = nombre
        self._apellido = apellido
        self._passwd = passwd
        self._mail = mail     
        self._tipo = tipo
        self._profesor = profesor
    
    def Id(self, value:int=None):
        if value != None:
            self._id = value
        return self._id
    
    def Nombre(self, value:str=None):
        if value != None:
            self._nombre = value
        return self._nombre
    
    def Apellido(self, value:str=None):
        if value != None:
            self._apellido = value
        return self._apellido
    
    def Mail(self, value:str=None):
        if value != None:
            self._mail = value
        return self._mail
    
    def Passwd(self, value:str=None):
        if value != None:
            self._pass = value
        return self._pass
    
    def Tipo(self, value:Tipo=None):
        if value != None:
            self._tipo = value
        return self._tipo
    
    def Nick(self, value:str=None):
        if value != None:
            self._nick = value
        return self._nick
    
    def toJson(self):
        if self._tipo == Tipo.Alumno:
            return {
                "id": self._id,
                "nick":self._nick,
                "nombre": self._nombre,
                "apellido": self._apellido,
                "mail": self._mail,
                "password": self._passwd,
                "tipo" : self._tipo.name
            }   
        else:
            return {
                "id": self._id,
                "nombre": self._nombre,
                "apellido": self._apellido,
                "mail": self._mail,
                "password": self._passwd,
                "tipo" : self._tipo.name,
                "tutor" : self._profesor.ToJson()['tutor'],
                "horario": self._profesor.ToJson()['horario'],
                "asignaturas": self._profesor.ToJson()['asignaturas']
            }  
            
            
class Clase:
    
    _clave: str
    _profesor: str
    _alumnos: list[str]
    _imagenes: list
    
    def __init__(self, clave:str = None, profesor:str = None, alumnos:list[str] = None, imagenes:list = []) -> None:
        self._clave = clave
        self._profesor = profesor
        self._alumnos = alumnos
        self._imagenes = imagenes
        
    def Clave(self, value:str = None):
        if value != None:
            self._clave = value
        return self._clave
    
    def Profesor(self, value:str = None):
        if value != None:
            self._profesor = value
        return self._profesor
    
    def Alumnos(self, value:list[str] = None):
        if value != None:
            self._alumnos = value
        return self._alumnos
    
    def addAlumno(self, value:str = None):
        if self.Alumnos() is not None:
            alumnos:list[str] = self.Alumnos()
        else:
            alumnos:list[str] = []
        alumnos.append(value)
        self._alumnos = alumnos
        
    def Imagenes(self, value = None):
        if value != None:
            self._imagenes = value
        return self._imagenes
    
    def addImage(self, img, username):
        self.Imagenes().append(username)
        path = os.getcwd()+'\\static\\attender\\'+username+'.png'
        with open(path, 'wb') as f:
            f.write(img.stream.read())
    
    def toJson(self):
        return {
                "clave": self._clave,
                "profesor": self._profesor,
                "alumnos": self._alumnos,
                "imagenes": self._imagenes
            }   