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
            data["tipo"] = user["tipo"]
            tokenData.update(data)
            return jwt.encode(tokenData, SECRET_KEY, algorithm='HS256') # Exactamente asi es en encode
            
    return jsonify("We do not do that here"), 400        
    #      try: porque cuando no se decodea lanza una excepcion
    #         jwt.decode(tokenData, SECRET_KEY, algorithms=['HS256']) Exactamente asi es el decode
# --------------------------------------------------------------------------------------------------

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
    data = request.get_json(silent=True)
   
    crearTarea(data)
    if "titulo" not in data or "tarea" not in data:
        return jsonify("Expected more from you"), 400
    return 
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

@application.route('/parking', methods=['GET'])
def parking():
    return "Not yet implemented"

@application.route('/discord', methods=['GET'])
def discord():
    return "Not yet implemented"

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

if __name__ == '__main__':
    application.run(debug=True,host='0.0.0.0')