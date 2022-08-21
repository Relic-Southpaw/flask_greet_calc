from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route('/add')
def both_add():
    a = int(request.args["a"])
    b = int(request.args["b"])
    total = add(a,b)
    return str(total)

@app.route('/sub')
def both_sub():
    a = int(request.args["a"])
    b = int(request.args["b"])
    total = sub(a,b)
    return str(total)

@app.route('/mult')
def both_mult():
    a = int(request.args["a"])
    b = int(request.args["b"])
    total = mult(a,b)
    return str(total)

@app.route('/div')
def both_div():
    a = int(request.args["a"])
    b = int(request.args["b"])
    total = div(a,b)
    return str(total)

MATHS ={
    "add": add,
    "sub": sub,
    "mult": mult,
    "div": div
}

@app.route('/math/<op>')
def math_do(op):
    a = int(request.args["a"])
    b = int(request.args["b"])

    total = MATHS[op](a,b)
    return str(total)
