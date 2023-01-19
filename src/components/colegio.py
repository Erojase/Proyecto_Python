
class Asignatura:

    _nombre: str
    _horasSemanales: int

    def __init__(self, nombre:str, horasSemanales:int) -> None:
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
    
    _nombre: str
    _tutor: bool
    _horario:list[int,int]
    _asignaturas: list[Asignatura]

    def __init__(self, tutor:bool, nombre:str, horario:list[int,int], asignaturas:list[Asignatura]):
        self._tutor = tutor
        self._nombre = nombre
        self._horario = horario
        self._asignaturas = asignaturas

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
    
    def Asignaturas(self, value:list[Asignatura]=None):
        if value != None:
            self._asignaturas = value 
        return self._asignaturas

    def ToJson(self) -> dict:
        json = {
            "nombre":self._nombre,
            "tutor":self._tutor,
            "horario":{
                        "inicio":self._asignaturas[0],
                        "fin":self._asignaturas[1]
                        },
            "asignaturas":self._asignaturas
        }
        return json



class Grupo:

    _asignaturas: list[Asignatura]
    _tutor: Profesor
    _profesores: list[Profesor]
    _horario: str

    def __init__(self) -> None:
        pass


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
    _hora: list[str,str]
    _grupo: Grupo
    _profesor: Profesor
