from factory import db

from flask_worker import WorkerMixin

def complex_task(seconds):
    import time
    print('Complex task started')
    for i in range(seconds):
        print('Progress: {}%'.format(100.0*i/seconds))
        time.sleep(1)
    print('Progress: 100.0%')
    print('Complex task finished')
    return 'Hello, World!'


# create a Worker model with the worker mixin
class Worker(WorkerMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    def __init__(self, name):
        super().__init__()
        self.name = name
        # set the worker's complex task along with args and kwargs
        self.set(complex_task, seconds=5)

def get_model(class_, name):
    return class_.query.filter_by(name=name).first() or class_(name)