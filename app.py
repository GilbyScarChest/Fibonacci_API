# Dependencies
from flask import Flask

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#### Calculating the Fibonacci numbers ####
# Start with a default number
n = 0

def fibo(n: int):
    if n < 1:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)

#################################################
# Routes
#################################################
@app.route("/")
def home():
    return (
        f"Available Routes:<br/>"
        f"/previous<br/>"
        f"/current<br/>"
        f"/next<br/>"

    )

@app.route("/current")
def current_fib():
    global n

    return str(fibo(n))

@app.route("/next")
def next_fib():
    global n
    n += 1

    return str(fibo(n))

@app.route("/previous")
def prev_fib():
    global n
    n -= 1

    return str(fibo(n))



if __name__ == '__main__':
    app.run()