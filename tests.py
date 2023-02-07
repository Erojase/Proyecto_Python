from src.components.colegio import *
from src.components.users import *
from src.services.scheduler import *
from src.services.dbManager import *
from src.services.serviceManager import *
from src.services.tasker import *

from datetime import datetime as d 
import json

asig1 = Asignatura("Moviles", 4)
asig2 = Asignatura("Servicios y procesos: VB", 3)
asig3 = Asignatura("Servicios y procesos: Python", 4)
asig4 = Asignatura("Desarrollo de Interfaces", 3)
asig5 = Asignatura("Ingles", 2)
asig6 = Asignatura("Empersa", 3)
asig7 = Asignatura("Navision", 3)
asig8 = Asignatura("Amazon", 2)
asig9 = Asignatura("Acceso a datos", 5)
asig10 = Asignatura("Big data", 2)

hor_prof1 = [["8", "21:30"], ["8","20:30"], ["8", "21:30"], ["8", "21:30"], ["8", "20:30"]]
list_prof1 = [asig7, asig8]
prof1 = Profesor(1,True, "Paco", hor_prof1, list_prof1)
hor_prof2 = [["8", "21:30"], ["8","21:30"], ["8", "21:30"], ["8", "21:30"], ["8", "20:30"]]
list_prof2 = [asig1, asig4]
prof2 = Profesor(2, False, "Guillermo", hor_prof2, list_prof2)
hor_prof3 = [["8", "21:30"], ["8","21:30"], ["8", "20:30"], ["8", "21:30"], ["8", "20:30"]]
list_prof3 = [asig3]
prof3 = Profesor(3, False, "David", hor_prof3, list_prof3)
hor_prof4 = [["8", "21:30"], ["8","21:30"], ["8", "21:30"], ["8", "21:30"], ["8", "20:30"]]
list_prof4 = [asig2]
prof4 = Profesor(4, False, "Tere", hor_prof4, list_prof4)
hor_prof5 = [["8", "21:30"], ["8","21:30"], ["8", "16:25"], ["8", "21:30"], ["8", "20:30"]]
list_prof5 = [asig5]
prof5 = Profesor(5, False, "Olga", hor_prof5, list_prof5)
hor_prof6 = [["8", "21:30"], ["8","21:30"], ["8", "21:30"], ["8", "21:30"], ["8", "19:40"]]
list_prof6 = [asig10]
prof6 = Profesor(6, False, "Luisa", hor_prof6, list_prof6)
hor_prof7 = [["8", "21:30"], ["8","21:30"], ["8", "21:30"], ["8", "21:30"], ["8", "20:30"]]
list_prof7 = [asig9]
prof7 = Profesor(7, False, "pedro", hor_prof7, list_prof7)
hor_prof8 = [["8", "21:30"], ["8","21:30"], ["8", "21:30"], ["8", "21:30"], ["8", "20:30"]]
list_prof8 = [asig6]
prof8 = Profesor(8, False, "Isabel/John", hor_prof8, list_prof8)

list_asignaturas1 = [asig1, asig2, asig3, asig4, asig5, asig6, asig7, asig8, asig9, asig10]
list_profesores1 = [prof1, prof2, prof3, prof4, prof5, prof6, prof7, prof8]
grp1 = Grupo("Dam-2b" ,list_asignaturas1, prof1, list_profesores1, "TARDE")

grp2 = Grupo("Dam-2a" ,list_asignaturas1, prof1, list_profesores1, "TARDE")

grp3 = Grupo("Dam-2c" ,list_asignaturas1, prof1, list_profesores1, "TARDE")

grp5 = Grupo("Dam-2e" ,list_asignaturas1, prof1, list_profesores1, "TARDE")

grp6 = Grupo("Dam-2f" ,list_asignaturas1, prof1, list_profesores1, "TARDE")

grp4 = Grupo("Dam-2d" ,list_asignaturas1, prof1, list_profesores1, "TARDE")


h1:Hora_horario = Hora_horario(asig1, d(2023, 10, 21, 13, 45, 00, 00), grp1, prof1)

if __name__ == '__main__':
    # bd:DbManager = DbManager()
    # task:Tarea = Tarea()

    # task.Nombre()
    # crearTarea()

    pass
    
