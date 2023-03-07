from flask import Flask, request, jsonify
import jwt
from datetime import datetime as dt, timedelta
from src.services.serviceManager import ServiceManager
from src.services.dbManager import DbManager
from src.services.tasker import *
from src.components.users import *

application = Flask(__name__)
db = DbManager()
sm = ServiceManager()
PATH_BASE = os.path.dirname(os.path.abspath(__file__))

SECRET_KEY = "JOYFE"

@application.route('/', methods=['GET','POST'])
def root():
    clientIp = request.remote_addr
    return f'server up -- your ip is {clientIp}'

@application.route('/web', methods=['GET'])
def webMain():
    return open('pages/index.html', 'r', encoding='utf-8')

@application.route('/login', methods=['GET'])
def webLogin():
    return open('pages/login.html', 'r', encoding='utf-8')

@application.route('/login', methods=['POST'])
def login():
    tokenData = {}
    data = request.get_json(silent=True)
    if "user" not in data or "password" not in data:
        return jsonify("Expected more from you"), 400
    
    # nombre_de_profesor = data["nombre"]
    
    for user in db.listUsers():
        if user["nick"] == data["user"] and user["password"] == data["password"]:
            tokenData = {"exp": dt.utcnow() + timedelta(days=1)} #expira en 1 dia
            data["id"] = user["id"]
            data["mail"] = user["mail"]
            data["tipo"] = user["tipo"] 
            del data['password']
            tokenData.update(data)
            return jwt.encode(tokenData, SECRET_KEY, algorithm='HS256') # Exactamente asi es en encode
            
    return jsonify("We do not do that here"), 400        
    #      try: porque cuando no se decodea lanza una excepcion
    #         jwt.decode(tokenData, SECRET_KEY, algorithms=['HS256']) Exactamente asi es el decode
# --------------------------------------------------------------------------------------------------

@application.route('/register', methods=['POST'])
def register():
    data = request.get_json(silent=True)
    if "user" not in data or "password" not in data:
        return jsonify("Expected more from you"), 400

    maxId = 0
    for user in db.listUsers():
        if user["id"] > maxId:
            maxId = user["id"]
    if data["tipo"] == Tipo.Alumno.name: 
        tmpUsr:Usuario = Usuario(maxId + 1, data["user"], "", "", data["password"], data["mail"], Tipo.Alumno)
    else:
        tmpUsr:Usuario = Usuario(maxId + 1, data["user"], "", "", data["password"], data["mail"], Tipo.Profesor)
    return  db.insertUser(tmpUsr)

@application.route('/testAction', methods=['POST'])
def testAction():
    print("Test Action Triggered")
    return "Test Action Triggered"

@application.route('/calendario', methods=['GET'])
def calendario():
    return open('pages/calendar.html', 'r', encoding='utf-8')




# ---------------------------------------------------------------------------------------------------


@application.route("/tasker",methods=['GET'])
def taskerr():
    return open('pages/tasker.html', 'r', encoding='utf-8')

@application.route("/tasker",methods=['POST'])
def tasker():
    token = request.headers['Authorization'].split()[1]
    user = parseToken(token)
    data = request.get_json(silent=True)
  
    tarea = crearTarea(data,user)
    if "titulo" not in data or "tarea" not in data:
        return jsonify("Expected more from you"), 400
    
    db.insertTarea(tarea)
    return 200
# ---------------------------------------------------------------------------------------------------




@application.route('/calTest', methods=['GET'])
def calTest():
    return sm.CalendarTestRun()

@application.route("/ponerTarea", methods=['POST'])
def ponerTatea():
    # data = request.get_json(silent=True)
    # sm.ponerTarea(data['Tarea'])
    return "Not yet implemented"

@application.route('/report', methods=['GET'])
def report():
    return "Not yet implemented"

@application.route('/attendance', methods=['GET'])
def asistencia():
    tipo = parseToken(request.args.get('token'))
    if tipo['tipo'] == Tipo.Profesor.name:
        return open('pages/attender_profesor.html', 'r', encoding='utf-8')
    elif tipo['tipo'] == Tipo.Alumno.name:
        return open('pages/attender_alumno.html', 'r', encoding='utf-8')


@application.route('/attendance', methods=['POST'])
def crear_buscar_clase():
    token = request.headers["Authorization"].split()[1]
    tokenData = parseToken(token)
    
    if tokenData['tipo'] == Tipo.Profesor.name:
        data = request.get_json(silent=True)
        profe:str = tokenData['user']
        alumnos = db.getAlumnos(data[1])
        return jsonify(sm.Crear_clase(data[0],profe, alumnos).toJson())
    elif tokenData['tipo'] == Tipo.Alumno.name:
        clave = request.headers["clave"]
        img = request.files.get("img")
        clase:Clase = sm.Buscar_clase_clave(clave)
        if clase != None:
            if tokenData["mail"] in clase.Alumnos():
                clase.Checked()[clase.Alumnos().index(tokenData["mail"])] = 1
                return "Checkeado"
            # if  clase.Alumnos() == None or tokenData['user'] not in clase.Alumnos():
            #     clase.addAlumno(tokenData['user'])
            #     clase.addImage(img, tokenData['user'])
                # return jsonify(clase.toJson())
        return ''

@application.route('/attendance/getclas', methods=['POST'])
def getclase():
    token = request.headers["Authorization"].split()[1]
    tipo = parseToken(token)
    if sm.Buscar_clase_profe(tipo['user']) != None:
        return jsonify(sm.Buscar_clase_profe(tipo['user']).toJson())
    return ''

@application.route('/attendance/hechar', methods=['POST'])
def hechar():
    token = request.headers["Authorization"].split()[1]
    tipo = parseToken(token)
    data = request.get_json(silent=True)
    
    return sm.Hechar_de_clase(tipo['user'], data)
    
@application.route('/attendance/fich', methods=['POST'])
def crear_fich():
    token = request.headers["Authorization"].split()[1]
    tipo = parseToken(token)
    data = request.get_json(silent=True)
    clase:Clase = sm.Buscar_clase_profe(tipo['user'])
    
    file = open(f'{PATH_BASE}/static/attender/Asistencia.txt','w')  
    if data == 'Presente':
        cont:int = 0
        for al in clase.Alumnos():
            if clase.Checked()[cont] == 1:
                comp:str = al.split('@')[0]
                apellidios:str = comp.split('.')[1] + ' ' + comp.split('.')[2]
                nombre:str = comp.split('.')[0]
                file.write(f'{apellidios} {nombre} \n')
            cont += 1
    else:
        cont:int = 0
        for al in clase.Alumnos():
            if clase.Checked()[cont] == 0:
                comp:str = al.split('@')[0]
                apellidios:str = comp.split('.')[1] + ' ' + comp.split('.')[2]
                nombre:str = comp.split('.')[0]
                file.write(f'{apellidios} {nombre} \n')
            cont += 1
            
    return 'Archivo creado'
    

@application.route('/attendance/mongo', methods=['GET'])
def getGrupos():
    return jsonify(db.getGrupos())


@application.route('/parking', methods=['GET'])
def parking():
    return "Not yet implemented"

@application.route('/bot', methods=['GET'])
def discord():
    return open('pages/bot.html', 'r', encoding='utf-8')

@application.route('/mail', methods=['GET'])
def mail():
    return open('pages/mail.html', 'r', encoding='utf-8')

@application.route('/sendMail', methods=['POST'])
def sendMail():
    data = request.get_json(silent=True)
    return "Not yet implemented"
    

@application.route('/listUsers', methods=['GET'])
def listUsers():
    users = db.listUsers()
    userlist = []
    for user in users:
        userlist.append(user['mail'])
    return jsonify(userlist)

@application.route('/token', methods=['POST'])
def token():
    authToken = request.headers["Authorization"].split()[1]
    data = parseToken(authToken)
    
    return data


def parseToken(token:str):
    data = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
    return data

def purgeTmpDirs():
    dirlist = os.listdir(os.getcwd()+'\\static\\attender\\')
    for dir in dirlist:
        os.remove(os.getcwd()+'\\static\\attender\\'+dir)

if __name__ == '__main__':
    purgeTmpDirs()
    application.run(debug=True,host='0.0.0.0')
    