from flask import Flask, Request, jsonify
from services.serviceManager import ServiceManager
from services.dbManager import DbManager
from components.profesor import Profesor

application = Flask(__name__)
db = DbManager()
sm = ServiceManager()


@application.route('/', methods=['GET','POST'])
def root():
    return 'server up'

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



if __name__ == '__main__':
    application.run(debug=True,host='0.0.0.0')