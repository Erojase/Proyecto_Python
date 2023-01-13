from flask import Flask

application = Flask(__name__)



@application.route('/', methods=['GET','POST'])
def root():
    return 'server up'

@application.route('/web', methods=['GET'])
def web():
    return open('pages/index.html', 'r')



if __name__ == '__main__':
    application.run(debug=True,host='0.0.0.0')