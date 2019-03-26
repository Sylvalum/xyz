from bottle import Bottle, route, run, template

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

run(app, host='localhost', port=8080)