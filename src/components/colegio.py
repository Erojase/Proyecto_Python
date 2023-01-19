class Profesor:
    
    _nombre: str
    _tutor: bool
    _horario:list[int,int]
    _asignaturas: list[str]

    def __init__(self):
        self._nombre = "Jamon"

    def Nombre(self, value:str=None):
        if value != None:
            self._nombre = value 
        return self._nombre
    
    def Tutor(self, value:bool=None):
        self._tutor = value if value != None else None
        return self._tutor
    
    def Horario(self, value:list[int,int]=None):
        if value != None:
            self._horario = value 
        return self._horario
    
    def Asignaturas(self, value:list[str]=None):
        if value != None:
            self._asignaturas = value 
        return self._asignaturas


class Asignatura:

    _nombre: str
    _horasSemanales: int

    def __init__(self) -> None:
        pass


class Grupo:

    _asignaturas: list[Asignatura]
    _tutor: Profesor
    _profesores: list[Profesor]
    _horario: str

    def __init__(self) -> None:
        pass
