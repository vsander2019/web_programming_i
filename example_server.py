from bottle import route, run, template

@route('/')
@route('/hello/<my_name>')
def get_hello(my_name="unknown person"):
<<<<<<< HEAD
    return(template("<html>Hello, {{name}}!!!<hr><html>",name = my_name))

@route('/goodbye')
def get_goodbye():
    return ("Well, goodbye, then!")
=======
    return(template("<html>Hello, {{name}}!!!<hr></html>",name=my_name))
    return("<html>Hello, {name}!!!<hr></html>".format(name=my_name))

@route('/goodbye')
def get_goodbye():
    return("Well, goodbye, then!")
>>>>>>> e9aa11123e0b7fefa36b747b132aa0c45326daca

run(host="localhost", port=8080)