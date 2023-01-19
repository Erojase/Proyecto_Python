from src.components.colegio import *
from src.services.dbManager import *
from src.services.serviceManager import *




if __name__ == '__main__':
    prof:Profesor = Profesor(False, "Paco",["19:00", "20:00"], ["Mates", "lengua"])
    
    print(prof.ToJson())