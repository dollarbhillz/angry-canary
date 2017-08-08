from flask import Flask
from flask import request

import requests


app = Flask(__name__)

# Returns cpu metrics.
@app.route('/cpu')
def get_cpu_stats():
    return str(psutil.cpu_times()) + '\n'


# Returns memory metrics.
@app.route('/memory')
def get_memory_stats():
    return str(psutil.virtual_memory()) + '\n'


# Returns disk metrics
# Warning: This does not currently work when within a container and will return
# an internal server error
@app.route('/disk')
def get_disk_io():
    return str(psutil.disk_usage()) + '\n'


# Simulate work being done and then return
@app.route('/do_work')
def do_work():
    fib(35)

    return "work finished"

# Recursively computes Fibonacci numbers for the sake of fake work
def fib(n):
    if n <= 1:
        return n
    else:


# Route hit by worker pods on success of busy work
@app.route('/success')
def success_query():
    return "nice jorb"


# Route hit by worker pods on failure of busy work
@app.route('/fail')
def success_query():
    return "ur dumb"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
