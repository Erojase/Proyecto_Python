class Profesor:
    
    _tutor:bool
    _horasMax:int
    _asignaturas:list[str]

    
    def __init__(self) -> None:
        if self._tutor:
            pass  
    
    def esTutor(self):
        return self._tutor

class Asignatura:
    
    _nombre:str
    _horasSemanales:int
    
    def __init__(self) -> None:
        pass

class Grupo:
    
    _asignaturas:list[Asignatura]
    _tutor:Profesor
    _profesores:list[Profesor]
    _horario:str
    
    def __init__(self) -> None:
        pass

