from bottle import route, run, template

@route('/')
@route('/hello/<my_name>')
def get_hello(my_name="unknown person"):
    return(template("<html>Hello, {{name}}!!!<hr><html>",name = my_name))

@route('/goodbye')
def get_goodbye():
    return ("Well, goodbye, then!")

run(host="localhost", port=8080)