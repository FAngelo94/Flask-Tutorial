from factory import create_app, db, socketio
from models import Worker, get_model

app = create_app()

# create database before first app request
@app.before_first_request
def before_first_request():
    db.create_all()

# VIEW FUNCTIONS GO HERE
@app.route('/')
@app.route('/index')
def index():
    worker = get_model(Worker, 'index')
    return worker.result if worker.job_finished else worker()

if __name__ == '__main__':
    socketio.run(app, debug=True)