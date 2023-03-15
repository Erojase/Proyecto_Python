from src.components.colegio import *
from src.services.scheduler import *
from src.services.attender import *
import json

class ServiceManager:
    
    def __init__(self) -> None:
        pass
    
    def Crear_clase(self, clave:str, profe:str, alumnos:list[str]) -> Clase:
        newclase:Clase = Clase(clave, profe, alumnos)
        checks = []
        for alumno in newclase.alumnos:
            checks.append(0)
            newclase.Checked(checks)
            arr_clas.append(newclase)
        
        return newclase
    
    def Buscar_clase_clave(self, clave:str) -> Clase:
        for clase in arr_clas:
            if clase.clave == clave:
                return clase
        return None
    
    def Buscar_clase_profe(self, profe:str) -> Clase:
        return buscar_clase_profe(profe)
    
    def Hechar_de_clase(self, profe:str, usuario:str) -> None:
        return hechar_de_clase(profe, usuario)
    
    def CalendarTestRun(self) -> dict:
        test = testRun()
        
        data = []
        semana = []
        dia = []
        
        for sem in test:
            semana = []
            for day in sem.horario:
                dia = []
                for hour in day.horario:
                    if hour.nombre is not None:
                        dia.append(hour.toJson())
                    else:
                        dia.append("None")
                semana.append(dia)
            data.append(semana)
        return json.dumps(data)
    
    def GenerarCalendar(self, grp:Grupo):
        return generar([grp])