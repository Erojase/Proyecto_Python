class Usuario:
    
    _id:int
    _nombre:str
    _apellido:str
    _passwd:str
    _mail:str
    
    
    def __init__(self, id:int, nombre:str, apellido:str, passwd:str, mail:str) -> dict:
        self._id = id
        self._nombre = nombre
        self._apellido = apellido
        self._passwd = passwd
        self._mail = mail     
    
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
    
    def toDict(self):
        return {
            "id": self._id,
            "nombre": self._nombre,
            "apellido": self._apellido,
            "mail": self._mail,
            "password": self._passwd
        }   