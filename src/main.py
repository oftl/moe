from bottle import route, run, template
import lib.math

@route ('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)

@route('/sqrt/<number>')
def sqrt (number):
    result = lib.math.sqrt (number)
    return template('<b>sqrt ({{number}}) = {{result}}</b>!', number=number, result=result)

run(host='localhost', port=8080)
