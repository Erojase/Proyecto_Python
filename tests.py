from src.components.colegio import *
from src.services.dbManager import *
from src.services.serviceManager import *




if __name__ == '__main__':
    bd:DbManager = DbManager()
    
    print(bd.listUsers())