from flask import Flask, request, jsonify
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


if __name__ == '__main__':
    application.run(debug=True,host='0.0.0.0')