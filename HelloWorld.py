from markupsafe import escape
from flask import Flask, request, render_template,url_for
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

@app.route('/post/<int:post_id>')
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
    return render_template('hello.html', name=name)

@app.route('/runscript')
def runscript():
    ManageScript.run()
    return 'CPP script run'

#Test printing in the console the results of test
with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))