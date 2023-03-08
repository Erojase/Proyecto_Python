from enum import Enum
import os
from src.components.colegio import *


class Tipo(Enum):
    Alumno = 0
    Profesor = 1


class Usuario:
    id: dict
    nick: str
    nombre: str
    apellido: str
    passwd: str
    mail: str
    tipo: Tipo

    profesor: Profesor | None

    def __init__(
        self,
        nick: str,
        nombre: str,
        apellido: str,
        passwd: str,
        mail: str,
        tipo: Tipo,
        profesor: Profesor | None = None,
        id: dict = None
    ) -> dict:
        self.id = id
        self._nick = nick
        self.nombre = nombre
        self.apellido = apellido
        self.passwd = passwd
        self.mail = mail
        self.tipo = tipo
        self.profesor = profesor

    def toJson(self):
        if self.tipo == Tipo.Alumno:
            return {
                "id": self.id,
                "nick": self.nick,
                "nombre": self.nombre,
                "apellido": self.apellido,
                "mail": self.mail,
                "password": self.passwd,
                "tipo": self.tipo.name,
            }
        else:
            self.profesor = Profesor(self.Id(), None, None, None, None)
            return {
                "id": self.id,
                "nick": self.nick,
                "nombre": self.nombre,
                "apellido": self.apellido,
                "mail": self.mail,
                "password": self.passwd,
                "tipo": self.tipo.name,
                "tutor": self.profesor.tutor,
                "horario": self.profesor.horario,
                "asignaturas": self.profesor.asignaturas,
            }


class Clase:
    clave: str
    profesor: str
    alumnos: list[str]
    checked: list[int]

    def __init__(
        self,
        clave: str = None,
        profesor: str = None,
        alumnos: list[str] = None,
        checked: list[int] = None,
    ) -> None:
        self.clave = clave
        self.profesor = profesor
        self.alumnos = alumnos
        self.checked = checked


    def addAlumno(self, value: str = None):
        if self.alumnos is not None:
            alumnos: list[str] = self.alumnos
        else:
            alumnos: list[str] = []
        alumnos.append(value)
        self.alumnos = alumnos

    def Checked(self, value=None):
        if value != None:
            self.checked = value
        return self.checked

    def toJson(self):
        return {
            "clave": self.clave,
            "profesor": self.profesor,
            "alumnos": self.alumnos,
            "checked": self.checked,
        }


class Tarea:
    id: int
    alumnos: list[str]
    asignatura: str
    descripcion: str
    profesor: str
    titulo: str

    def __init__(
        self,
        id: int = None,
        alumnos: list[str] = [],
        asignatura: str = None,
        descripcion: str = None,
        profesor: str = None,
        titulo: str = None,
    ) -> None:
        self.id = id
        self.alumnos = alumnos
        self.asignatura = asignatura
        self.descripcion = descripcion
        self.profesor = profesor
        self.titulo = titulo

    def toJson(self):
        return {
            "asignatura": self.asignatura,
            "profesor": self.profesor,
            "titulo": self.alumnos,
            "descripcion": self.descripcion,
        }
