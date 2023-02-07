from src.components.colegio import *
from src.services.scheduler import *
import json

class ServiceManager:
    
    def __init__(self) -> None:
        pass
    
    
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