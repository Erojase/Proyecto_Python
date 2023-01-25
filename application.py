from flask import Flask, request, jsonify
import jwt
from datetime import datetime, timedelta
from src.services.serviceManager import ServiceManager
from src.services.dbManager import DbManager

application = Flask(__name__)
db = DbManager()
sm = ServiceManager()


@application.route('/', methods=['GET','POST'])
def root():
    clientIp = request.remote_addr
    return f'server up -- your ip is {clientIp}'

@application.route('/web', methods=['GET'])
def web():
    return open('pages/index.html', 'r')

@application.route('/calendario', methods=['GET'])
def calendario():
    return  db.listUsers()

@application.route('/testAction', methods=['POST'])
def testAction():
    print("Test Action Triggered")
    return "Test Action Triggered"

@application.route('/login', methods=['POST'])
def login():
    data = request.get_json(silent=True)
    request.headers
    # Comprobar si existe y esas cosas
    tokenData = {
        "id": 1,
        "exp": datetime.utcnow() + timedelta(seconds=1) #expira en 1 segundo
    }
    SECRET_KEY = "JOYFE"
    return jwt.encode(tokenData, SECRET_KEY, algorithm='HS256') # Exactamente asi es en encode
    #      try: porque cuando no se decodea lanza una excepcion
    #         jwt.decode(tokenData, SECRET_KEY, algorithms=['HS256']) Exactamente asi es el decode

if __name__ == '__main__':
    application.run(debug=True,host='0.0.0.0')