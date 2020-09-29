from markupsafe import escape
from flask import Flask, request, render_template,url_for, redirect,make_response, session, abort, flash
from flask_cors import CORS

import ManageScript

app = Flask(__name__)
CORS(app)

# Routing
@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello, World'

# Variable Rules
@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % escape(username)

@app.route('/post/<int:post_id>') #types we can use: string (default), int, float, path, any, uuid
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return 'Subpath %s' % escape(subpath)

#Unique URLs / Redirection Behavior
@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'
    
#HTTP Methods
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return "POST Login"
    else:
        return "GET Logic"

#Rendering Templates
@app.route('/hello2/')
@app.route('/hello2/<name>')
def hello2(name=None):
    dict ={'phy':50,'che':60,'maths':70}
    return render_template('hello.html', name=name, result=dict)

@app.route('/runscript')
def runscript():
    ManageScript.run()
    return 'CPP script run'

#Test printing in the console the results of test
with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))

#add_url_rule
def home():
    return "Homepage"
app.add_url_rule('/home', 'home', home)

#redurect example
@app.route('/admin')
def hello_admin():
    return 'Hello Admin'

@app.route('/typeuser/<name>')
def typeuser(name):
    if(name == 'admin' ):
        return redirect(url_for('hello_admin'))
    else:
        return "Basic User"

# Error example
@app.route('/error/')
def error():
    abort(401) #there are a lot of different code

# Use static script in template
@app.route('/button/')
def button():
    return render_template('button.html')

# Cookie example
@app.route('/indexcookie')
def indexcookie():
    return render_template('setcookie.html')

@app.route('/setcookie',methods=['POST','GET'])
def setcookie():
    if request.method == 'POST':
        user = request.form['nm']
        resp= make_response(render_template('readcookie.html'))
        resp.set_cookie('userID',user)
        return resp

@app.route('/getcookie')
def getcookie():
    name = request.cookies.get('userID')
    return '<h1>Welcome '+name+'</h1>'

# Session example
app.secret_key="key secret for session"
@app.route('/setsession')
def setsession():
    session['username'] = 'Angelo'
    return "session name set"

@app.route('/getsession')
def getsession():
    if(session):
        return "session name = " + session['username']
    return "no username"

@app.route('/deletesession')
def deletesession():
    session.pop('username', None)
    return "session name deleted"

# Message flashing example
@app.route('/messageflashing/')
def messageflashing():
    flash("Test flash message")
    return render_template('flash.html')



if __name__ == '__main__':
    host='127.0.0.1' # Set 0.0.0.0 to have server available externally
    port=5000
    app.run(host=host, port=port, debug=True) # Active debug for the server, it refreshes when there are updates