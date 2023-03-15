from flask import Flask, request, jsonify
import jwt
import json
from datetime import datetime as dt, timedelta
from src.services.serviceManager import ServiceManager
from src.services.dbManager import DbManager
from src.components.users import *

application = Flask(__name__)
db = DbManager()
sm = ServiceManager()
PATH_BASE = os.path.dirname(os.path.abspath(__file__))

SECRET_KEY = "JOYFE"


# Root endpoint
@application.route('/', methods=['GET','POST'])
def root():
    clientIp = request.remote_addr
    return f'server up -- your ip is {clientIp}'

# Landing Page
@application.route('/web', methods=['GET'])
def webMain():
    return open('pages/index.html', 'r', encoding='utf-8')

# Login endpoints
@application.route('/login/auth', methods=['POST'])
def googleAuth():
    data = parseToken(request.get_data().decode(encoding="utf-8").split('=')[1].split('&')[0], False) 
    tkdata = {}
    token = ""
    
    user = db.getOneUser({"mail":data["email"]},{"_id":0})
    if user is not None:
        token = {"exp": dt.utcnow() + timedelta(days=1)} #expira en 1 dia
        tkdata["tipo"] = user["tipo"]
        tkdata["mail"] = user["mail"]
        tkdata["nick"] = user["nick"]
        token.update(tkdata)
    if token == "":
        return "<html><script>window.localStorage.removeItem('token'); window.location.href = '/login'; </script></html>"
    codedToken = jwt.encode(token, SECRET_KEY, algorithm='HS256')
    return "<html><script>window.localStorage.setItem('token', '"+codedToken+"'); window.location.href = '/web'; </script></html>"

@application.route('/login', methods=['GET'])
def webLogin():
    return open('pages/login.html', 'r', encoding='utf-8')

@application.route('/login', methods=['POST'])
def login():
    tokenData = {}
    data = request.get_json(silent=True)
    if "nick" not in data or "password" not in data:
        return jsonify("Expected more from you"), 400
    
    user = db.getOneUser({"nick":data["nick"], "password":data["password"]},{"_id":0})
    if user is not None:
        tokenData = {"exp": dt.utcnow() + timedelta(days=1)} #expira en 1 dia
        data["mail"] = user["mail"]
        data["tipo"] = user["tipo"] 
        del data['password']
        tokenData.update(data)
        return jwt.encode(tokenData, SECRET_KEY, algorithm='HS256')
            
    return jsonify("We do not do that here"), 400        


# Register endpoints
@application.route('/register', methods=['POST'])
def register():
    data = request.get_json(silent=True)
    if "user" not in data or "password" not in data:
        return jsonify("Expected more from you"), 400
    

    if data["tipo"] == Tipo.Alumno.name: 
        tmpUsr:Usuario = Usuario(data["user"], None, None, data["password"], data["mail"], Tipo.Alumno)
    else:
        tmpUsr:Usuario = Usuario(data["user"], None, None, data["password"], data["mail"], Tipo.Profesor)
    return  db.insertUser(tmpUsr)


# Calendar endpoints
@application.route('/calendario', methods=['GET'])
def calendario():
    return open('pages/calendar.html', 'r', encoding='utf-8')

@application.route('/calTest', methods=['GET'])
def calTest():
    return sm.CalendarTestRun()

@application.route('/horario/mongo/profesores', methods=['GET'])
def getProfesores():
    return jsonify(db.getProfesores())

@application.route('/horario/mongo/asignaturas', methods=['GET'])
def getAsignaturas():
    return jsonify(db.getAsignaturas())

@application.route('/horario/mongo/crear', methods=['POST'])
def crearGrupo():
    data = request.get_json(silent=True)
    return jsonify(db.crearGrupo(Grupo(data["nombre"], data["asignaturas"], data["tutor"], data["profesores"], data["horario"])))




# Attendance endpoints
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
        profe:str = tokenData['nick']
        alumnos = db.getAlumnos(data[1])
        return jsonify(db.crearClase(db.historicoCrear(alumnos, profe), alumnos, profe, data[0]))
    elif tokenData['tipo'] == Tipo.Alumno.name:
        clave = request.headers["clave"]
        img = request.files.get("img")
        clase:Clase = sm.Buscar_clase_clave(clave)
        if clase != None:
            if tokenData["mail"] in clase.Alumnos():
                clase.Checked()[clase.Alumnos().index(tokenData["mail"])] = 1
                return "Checkeado"
        return ''

@application.route('/attendance/getclass', methods=['POST'])
def getclase():
    token = request.headers["Authorization"].split()[1]
    tipo = parseToken(token)
    if sm.Buscar_clase_profe(tipo['nick']) != None:
        return jsonify(sm.Buscar_clase_profe(tipo['nick']).toJson())
    return ''
    
@application.route('/attendance/fichero', methods=['POST'])
def crear_fich():
    token = request.headers["Authorization"].split()[1]
    tipo = parseToken(token)
    data = request.get_json(silent=True)
    clase:Clase = sm.Buscar_clase_profe(tipo['nick'])
    
    file = open(f'{PATH_BASE}/static/attender/Asistencia.txt','w')  
    if data == 'Presente':
        cont:int = 0
        for al in clase.alumnos:
            if clase.Checked()[cont] == 1:
                comp:str = al.split('@')[0]
                apellidios:str = comp.split('.')[1] + ' ' + comp.split('.')[2]
                nombre:str = comp.split('.')[0]
                file.write(f'{apellidios} {nombre} \n')
            cont += 1
    else:
        cont:int = 0
        for al in clase.alumnos:
            if clase.Checked()[cont] == 0:
                comp:str = al.split('@')[0]
                apellidios:str = comp.split('.')[1] + ' ' + comp.split('.')[2]
                nombre:str = comp.split('.')[0]
                file.write(f'{apellidios} {nombre} \n')
            cont += 1
            
    return 'Archivo creado'

@application.route('/listUsers', methods=['GET'])
def listUsers():
    users = db.getOneUser({},{"_id":0,"mail":1})
    return jsonify(list(users))    

@application.route('/attendance/mongo', methods=['GET'])
def getGrupos():
    return jsonify(db.getGrupos())




# Discord bot
@application.route('/bot', methods=['GET'])
def discord():
    return open('pages/bot.html', 'r', encoding='utf-8')




# User information endpoint
@application.route('/info', methods=['GET'])
def userInfo():
    return open('pages/info.html', 'r', encoding='utf-8')

@application.route('/info/<nick>', methods=['GET'])
def currentUserInfo(nick:str):
    authToken = request.headers["Authorization"].split()[1]
    data = parseToken(authToken)
    if nick == data["nick"]:
        info = db.getOneUser({"nick":nick},{"_id":0})
        return jsonify(info)
    else:
        return "User not authorized to do this action", 400

@application.route('/info/update/<nick>', methods=['PUT'])
def UpdateUser(nick):
    authToken = request.headers["Authorization"].split()[1]
    token = parseToken(authToken)
    data = request.get_json(silent=True)
    
    if nick == token["nick"]:
        jamon = db.updateUser({"nick":nick},data)
        return jsonify(jamon)
    else:
        return "User not authorized to do this action", 400

# Utils
def parseToken(token:str, verify_signature=True):
    data = jwt.decode(token, SECRET_KEY, algorithms=['HS256'], options={"verify_signature": verify_signature})
    return data

def purgeTmpDirs():
    if not os.path.exists(os.getcwd()+'\\static\\attender\\'):
        os.mkdir(os.getcwd()+'\\static\\attender\\')
        
    dirlist = os.listdir(os.getcwd()+'\\static\\attender\\')
    for dir in dirlist:
        os.remove(os.getcwd()+'\\static\\attender\\'+dir)



if __name__ == '__main__':
    purgeTmpDirs()
    application.run(debug=True,host='0.0.0.0')
    