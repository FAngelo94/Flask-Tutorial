from markupsafe import escape
from flask import Flask, request, render_template,url_for, redirect,make_response, session, abort, flash
from flask_caching import Cache
from multiprocessing import Pool, TimeoutError
import time
import os

config = {
    "DEBUG": True,          # some Flask specific configs
    "CACHE_TYPE": "filesystem", # Flask-Caching related configs
    "CACHE_DEFAULT_TIMEOUT": 300,
    "CACHE_DIR": r"C:\Users\User\Desktop\Angelo\Project\Paxmile\Flask\mycache"
}

cache = Cache(config=config)

app = Flask(__name__)
cache.init_app(app)

@app.route('/')
def index():
    return 'Index Page'

# Caching a function and use it
# @cache.memoize(300) #time in seconds
def messageflashing(x=1):
    print("message ",x,"-",os.getpid())
    j = 0
    for i in range(1,100000000):
        j += i
    print("finished ",x,"-",os.getpid())
    return x*2

@app.route('/usecachingfunctionwithworker/<int:x>')
def usecachingfunctionwithworker(x):
    print(cache.get("save"))
    calc_x = str(messageflashing(x))
    cache.set("save", calc_x)
    with Pool(processes=8) as pool:
        print(pool.map(messageflashing, range(x)))
        print("For the moment, the pool remains available for more work")
    print("Now the pool is closed and no longer available")
    return 'X= ' + calc_x

@app.route('/usecachingfunctionwithworkerasync/<int:x>')
def usecachingfunctionwithworkerasync(x):
    print(cache.get("save"))
    calc_x = str(messageflashing(x))
    cache.set("save", calc_x)
    with Pool(processes=4) as pool:
        print(pool.map_async(messageflashing, range(x)))
        print("For the moment, the pool remains available for more work")
        pool.close()
        pool.join()
    print("Now the pool is closed and no longer available")
    print('X= ' + calc_x)
    return 'X= ' + calc_x

@app.route('/usecachingfunctionwithworkerasync2/<int:x>')
def usecachingfunctionwithworkerasync2(x):
    print(cache.get("save"))
    calc_x = str(messageflashing(x))
    cache.set("save", calc_x)
    pool = Pool(processes=4)
    pool.map_async(messageflashing, range(x))
    print("For the moment, the pool remains available for more work")
    # Commenting the following 2 row the methods finish but workers run asyncronus
    # pool.close()
    # pool.join()
    print("Now the pool is closed and no longer available")
    print('X= ' + calc_x)
    return 'X= ' + calc_x

if __name__ == '__main__':
    host='127.0.0.1' # Set 0.0.0.0 to have server available externally
    port=5000
    app.run(host=host, port=port, debug=True) # Active debug for the server, it refreshes when there are updates