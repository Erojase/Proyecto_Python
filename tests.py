from src.components.colegio import *
from src.services.horarioGenerator import *
from src.services.dbManager import *
from src.services.serviceManager import *

asig1 = Asignatura("Moviles", 4)
asig2 = Asignatura("Servicios y procesos", 7)
asig3 = Asignatura("Desarrollo de Interfaces", 3)
asig4 = Asignatura("Ingles", 2)
asig5 = Asignatura("Empersa", 3)
asig6 = Asignatura("Navision", 3)
asig7 = Asignatura("Amazon", 2)
asig8 = Asignatura("Acceso a datos", 5)
asig9 = Asignatura("Big data", 2)

hor_prof1 = [["8", "14:30"], ["8","20:30"], ["8", "14:30"], ["8", "14:30"], ["8", "14:30"]]
list_prof1 = [asig6, asig7]
prof1 = Profesor(True, "Paco", hor_prof1, list_prof1)
hor_prof2 = [["8", "16:30"], ["8","15:25"], ["8", "15:25"], ["8", "16:30"], ["8", "15:25"]]
list_prof2 = [asig1, asig3]
prof2 = Profesor(False, "Guillermo", hor_prof2, list_prof2)
hor_prof3 = [["8", "14:30"], ["8","14:30"], ["8", "20:30"], ["8", "14:30"], ["8", "14:30"]]
list_prof3 = [asig2]
prof3 = Profesor(True, "David", hor_prof3, list_prof3)
hor_prof4 = [["8", "17:20"], ["8","14:30"], ["8", "14:30"], ["8", "14:30"], ["8", "17:20"]]
list_prof4 = [asig2]
prof4 = Profesor(True, "Tere", hor_prof4, list_prof4)
hor_prof5 = [["8", "18:40"], ["8","14:30"], ["8", "16:25"], ["8", "14:30"], ["8", "14:30"]]
list_prof5 = [asig4]
prof5 = Profesor(True, "Olga", hor_prof5, list_prof5)
hor_prof6 = [["8", "14:30"], ["8","14:30"], ["8", "14:30"], ["8", "14:30"], ["8", "19:40"]]
list_prof6 = [asig9]
prof6 = Profesor(True, "Luisa", hor_prof6, list_prof6)
hor_prof7 = [["8", "14:30"], ["8","14:30"], ["8", "14:30"], ["8", "21:30"], ["8", "14:30"]]
list_prof7 = [asig8]
prof7 = Profesor(True, "Pedro", hor_prof7, list_prof7)

list_asignaturas1 = [asig1, asig2, asig3, asig4, asig5, asig6, asig7, asig8, asig9]
list_profesores1 = [prof1, prof2, prof3, prof4, prof5, prof6, prof7]
grp1 = Grupo(list_asignaturas1, prof1, list_profesores1, "TARDE")


if __name__ == '__main__':
    bd:DbManager = DbManager()
    
    print(bd.listUsers())
    generar(grp1)
    
    pass
