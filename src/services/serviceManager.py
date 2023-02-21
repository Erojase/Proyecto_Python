from src.components.colegio import *
from src.services.scheduler import *
from src.services.attender import *
import json

class ServiceManager:
    
    def __init__(self) -> None:
        pass
    
    def Crear_clase(self, clave:str, profe:str) -> None:
        return crear_clase(clave, profe)
    
    def Buscar_clase_clave(self, clave:str) -> Clase:
        return buscar_clase_clave(clave)
    
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
            for day in sem.Horario():
                dia = []
                for hour in day.Horario():
                    if hour.Nombre() is not None:
                        dia.append(hour.toJson())
                    else:
                        dia.append("None")
                semana.append(dia)
            data.append(semana)
        return json.dumps(data)