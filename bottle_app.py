import datetime
import time
<<<<<<< HEAD
import os
import random
import sqlite3
=======
>>>>>>> b2693012a90410afe5705293c2236191d9d3b702
import uuid
import dataset
import json

db = dataset.connect('sqlite:///todo.db')

from bottle import get, post, request, response, template, redirect, default_app

def get_session(request, response):
    session_id = request.cookies.get("session_id",None)
    if session_id == None:
        session_id = str(uuid.uuid4())
        session = { 'session_id':session_id, "username":"Guest", "time":int(time.time()) }
        db['session'].insert(session)
        response.set_cookie("session_id",session_id)
    else:
        session=db['session'].find_one(session_id=session_id)
        if session == None:
            session_id = str(uuid.uuid4())
            session = { 'session_id':session_id, "username":"Guest", "time":int(time.time()) }
            db['session'].insert(session)
            response.set_cookie("session_id",session_id)

            # session = {"message":"no session found with the id =" + session_id}
    return session

def save_session(session):
    db['session'].update(session,['session_id'])

@get('/login')
def get_login():
    session = get_session(request, response)
    if session['username'] != 'Guest':
        redirect('/')
        return
    return template("login", csrf_token="abcrsrerredadfa")

@post('/login')
def post_login():
    session = get_session(request, response)
    if session['username'] != 'Guest':
        redirect('/')
        return
    # csrf_token = request.forms.get("csrf_token").strip()
    # if csrf_token != "abcrsrerredadfa":
    #     redirect('/login_error')
    #     return
    username = request.forms.get("username").strip()
    password = request.forms.get("password").strip()
    profile = db['profile'].find_one(username=username)
    if profile == None:
        redirect('/login_error')
        return
    if password != profile["password"]:
        redirect('/login_error')
        return
    session['username'] = username
    save_session(session)
    redirect('/')


@get('/logout')
def get_logout():
    session = get_session(request, response)
    session['username'] = 'Guest'
    save_session(session)
    redirect('/login')

@get('/register')
def get_register():
    session = get_session(request, response)
    if session['username'] != 'Guest':
        redirect('/')
        return
    return template("register", csrf_token="abcrsrerredadfa")

@post('/register')
def post_register():
    session = get_session(request, response)
    if session['username'] != 'Guest':
        redirect('/')
        return
    # csrf_token = request.forms.get("csrf_token").strip()
    # if csrf_token != "abcrsrerredadfa":
    #     redirect('/login_error')
    #     return
    username = request.forms.get("username").strip()
    password = request.forms.get("password").strip()
    if len(password) < 8:
        redirect('/login_error')
        return
    profile = db['profile'].find_one(username=username)
    if profile:
        redirect('/login_error')
        return
    db['profile'].insert({'username':username, 'password':password})
    redirect('/')


@get('/')

def get_show_list():
<<<<<<< HEAD

    # ask for cookie, if we don't have one start a guest session
    session_id = request.cookies.get("session_id",None)
    if session_id == None:
        session_id = str(uuid.uuid4())
        session = {'session_id':session_id, "username":"Guest", "time":int(time.time())}
        db.insert(session)
        response.set_cookie("session_id",session_id)
    # had a cookie with an id, look up the session
    else:
        result = db.search(query.session_id == session_id)
        # the session isn't found, start a new one
        if len(result) == 0:
            session_id = str(uuid.uuid4())
            session = {'session_id':session_id, "username":"Guest", "time":int(time.time())}
            db.insert(session)
            response.set_cookie("session_id",session_id)
        # the session is found, use it
        else:
            session=result[0]

    connection = sqlite3.connect("todo.db")
    cursor = connection.cursor()
    cursor.execute("select * from todo")
    result = cursor.fetchall()
    cursor.close()
    return template("show_list", rows=result, session={})


@get('/sandbox')
def get_sandbox():
    return template("sandbox")

@get('/ajaxdemo')
def get_ajaxdemo():
    return template("ajaxdemo")

@get('/jquerydemo')
def get_jquerydemo():
    return template("jquerydemo")


@get('/login')
def get_login():
    return template("login", crsf_token="abc")

@post('/login')
def post_login():
    crsf_token = request.forms.get("crsf_token").strip()
    if crsf_token != "abc":
        redirect('/login_error')
    username = request.forms.get("username").strip()
    password = request.forms.get("password").strip()
    if password != "password":
        redirect('/login_error')
    session_id = request.cookies.get("session_id",str(uuid.uuid4()))
    result = db.search(query.session_id == session_id)
    if len(result) == 0:
        db.insert({'session_id':session_id, 'username':username})
    else:
        session = result[0]
        db.update({'username':username},query.session_id == session_id)
    response.set_cookie("session_id",session_id)
    redirect('/')

@get('/logout')
def get_logout():
    session_id = request.cookies.get("session_id",str(uuid.uuid4()))
    result = db.search(query.session_id == session_id)
    if len(result) == 0:
        db.insert({'session_id':session_id, 'username':username})
    else:
        session = result[0]
        db.update({'username': "Unknown"},query.session_id == session_id)
    response.set_cookie("session_id",session_id)
    redirect('/')



@get('/login_error')
def get_login_error():
    return template("login_error")

@get('/set_status/<id:int>/<value:int>')
def get_set_status(id, value):
    connection = sqlite3.connect("todo.db")
    cursor = connection.cursor()
    cursor.execute("update todo set status=? where id=?", (value, id,))
    connection.commit()
    cursor.close()
=======
    session = get_session(request, response)
    if session['username'] == 'Guest':
        redirect('/login')
        return
    result = db['todo'].all()
    result=[dict(r) for r in result]
    return template("show_list", rows=result, session=session)

@get('/show_list_ajax')
def get_show_list_ajax():
    session = get_session(request, response)
    if session['username'] == 'Guest':
        redirect('/login')
        return
    return template("show_list_ajax", session=session)

@get('/get_tasks')
def get_get_tasks():
    session = get_session(request, response)
    response.content_type = 'application/json'
    if session['username'] == 'Guest':
        return "[]"
    else:
        result = db['todo'].all()
        tasks= [dict(r) for r in result]
        # tasks = [
        #     {"id" : 1, "task": "do something interesting", "status":False },
        #     {"id" : 2, "task": "do something enjoyable", "status":False },
        #     {"id" : 3, "task": "do something useful", "status":False }
        #     ]
        text = json.dumps(tasks)
        return text

@get('/update_status/<id:int>/<value:int>')
def get_update_status(id, value):
    session = get_session(request, response)
    if session['username'] == 'Guest':
        redirect('/login')
        return
    #result = db['todo'].find_one(id=id)
    db['todo'].update({'id':id, 'status':(value!=0)},['id'])
>>>>>>> b2693012a90410afe5705293c2236191d9d3b702
    redirect('/')


@get('/delete_item/<id:int>')
def get_delete_item(id):
    session = get_session(request, response)
    if session['username'] == 'Guest':
        redirect('/login')
        return
    db['todo'].delete(id=id)
    redirect('/')


@get('/update_task/<id:int>')
def get_update_task(id):
    session = get_session(request, response)
    if session['username'] == 'Guest':
        redirect('/login')
        return
    result = db['todo'].find_one(id=id)
    return template("update_task", row=result)


@post('/update_task')
def post_update_task():
    session = get_session(request, response)
    if session['username'] == 'Guest':
        redirect('/login')
        return
    id = int(request.forms.get("id").strip())
    updated_task = request.forms.get("updated_task").strip()
    db['todo'].update({'id':id, 'task':updated_task},['id'])
    redirect('/')


@get('/new_item')
def get_new_item():
    session = get_session(request, response)
    if session['username'] == 'Guest':
        redirect('/login')
        return
    return template("new_item")


@post('/new_item')
def post_new_item():
    session = get_session(request, response)
    if session['username'] == 'Guest':
        redirect('/login')
        return
    new_task = request.forms.get("new_task").strip()
    db['todo'].insert({'task':new_task, 'status':False})
    redirect('/')


<<<<<<< HEAD
if ON_PYTHONANYWHERE:
    application = default_app()
else:
    debug(True)
    run(host="localhost", port=8080)
=======
application = default_app()


if __name__ == "__main__":
    #print(get_show_list())
    get_update_task(6)
>>>>>>> b2693012a90410afe5705293c2236191d9d3b702
