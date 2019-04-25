from bottle import Bottle, route, run, template
from gevent import monkey; monkey.patch_all()
import os, time

app = Bottle()

@app.route('/sum/<num1>/<num2>')
def sum(num1, num2):
    total = str(int(num1) + int(num2))
    print(total)
    return template('<b>{{total}}</b>', total=total)

@app.route('/sub/<num1>/<num2>')
def sub(num1, num2):
    total = str(int(num1) - int(num2))
    print(total)
    return template('<b>{{total}}</b>', total=total)
	
@app.get('/asdf')
def asdf():
	time.sleep(10)
	return 'hola'
	
@app.get('/david')
def asdf():
	return template('template_david')

port = os.environ.get('PORT', 5000)
run(app, host='0.0.0.0', port=port, server='gevent')