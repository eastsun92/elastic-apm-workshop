from flask import Flask, jsonify, Response
from elasticapm.contrib.flask import ElasticAPM

import time

app = Flask(__name__)

## TODO
app.config['ELASTIC_APM'] = {
  'SERVICE_NAME': '',
  'SECRET_TOKEN': '',
  'SERVER_URL': '',
  'ENVIRONMENT': '',
}

# app.debug = True
apm = ElasticAPM(app)

@app.route('/')
def index():
    return 'Web App with Python Flask!1 !'

@app.route('/1')
def index1():
    time.sleep(0.1)
    return '0.1 sec'

@app.route('/2')
def index2():
    time.sleep(0.2)
    return '0.2 sec'

@app.route('/3')
def index3():
    time.sleep(0.3)
    return '0.3 sec'

@app.route('/4')
def index4():
    time.sleep(0.4)
    return '0.4 sec'

@app.route('/5')
def index5():
    time.sleep(0.5)
    return '0.5 sec'

@app.route('/6')
def index6():
    time.sleep(0.6)
    return '0.6 sec'

@app.route('/7')
def index7():
    time.sleep(0.7)
    return '0.7 sec'

@app.route('/8')
def index8():
    time.sleep(0.8)
    return '0.8 sec'

@app.route('/9')
def index9():
    time.sleep(0.9)
    return '0.9 sec'

@app.route('/10')
def index10():
    time.sleep(1)
    return '1 sec'

@app.route('/11')
def index11():
    time.sleep(1.5)
    return '1.5 sec'

@app.route('/12')
def index12():
    time.sleep(2)
    return '2 sec'

@app.route('/13')
def index13():
    time.sleep(2.5)
    return '2.5 sec'

@app.route('/14')
def index14():
    time.sleep(3)
    return '3 sec'

@app.route('/15')
def index15():
    time.sleep(3.5)
    resp = flask.Response("hello world")
    resp.headers['Access-Control-Allow-Origin'] = '*' 
    return resp

app.run(host='0.0.0.0', port=81)
