from flask import Flask, request, jsonify
import jwt
from datetime import datetime, timedelta
from src.services.serviceManager import ServiceManager
from src.services.dbManager import DbManager

application = Flask(__name__)
db = DbManager()
sm = ServiceManager()

SECRET_KEY = "JOYFE"

@application.route('/', methods=['GET','POST'])
def root():
    clientIp = request.remote_addr
    return f'server up -- your ip is {clientIp}'

@application.route('/web', methods=['GET'])
def web():
    return open('pages/index.html', 'r')

# --------------------------------------------------------------------------------------------------

# @application.route('/testAction', methods=['POST'])
# def testAction():
#     print("Test Action Triggered")
#     return "Test Action Triggered"

@application.route('/calendario', methods=['GET'])
def calendario():
    return  db.listUsers()
    
@application.route('/report', mehtods=[''])#<--- tipo de metodos
def report():
    return  # no terminadpo

@application.route('/asistencia', mehtods=[''])#<--- tipo de metodos
def report():
    return  # no terminadpo

@application.route('/parking', mehtods=[''])#<--- tipo de metodos
def report():
    return  # no terminadpo

@application.route('/discord', mehtods=[''])#<--- tipo de metodos
def report():
    return  # no terminadpo

@application.route('/mail', mehtods=[''])#<--- tipo de metodos
def report():
    return  # no terminadpo


@application.route('/login', methods=['POST'])
def login():
    data = request.get_json(silent=True)
    request.headers
    # Comprobar si existe y esas cosas
    tokenData = {
        "id": 1,
        "exp": datetime.utcnow() + timedelta(seconds=1) #expira en 1 segundo
    }
    
    return jwt.encode(tokenData, SECRET_KEY, algorithm='HS256') # Exactamente asi es en encode
    #      try: porque cuando no se decodea lanza una excepcion
    #         jwt.decode(tokenData, SECRET_KEY, algorithms=['HS256']) Exactamente asi es el decode

@application.route('/user/profile')
def userProfile():
    authToken = request.headers["Authorization"].split()[1]
    data = jwt.decode(authToken, SECRET_KEY, algorithms=['HS256'])
    
    userdata = db.getUser(data["id"])
    
    if data["id"] in userdata:
        return jsonify(userdata)


if __name__ == '__main__':
    application.run(debug=True,host='0.0.0.0')