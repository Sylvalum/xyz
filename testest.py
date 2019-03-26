from bottle import route, run, template

@route('/sum/<num1>/<num2>')
def index(num1, num2):
    total = str(int(num1) + int(num2))
    logging.info(total)
    return template('<b>{{total}}</b>', total=total)

run(host='localhost', port=8080)