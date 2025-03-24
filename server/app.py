#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:parameter>')
def print_parameter(parameter):
    print(parameter)
    return parameter

@app.route('/count/<int:parameter>')
def count(parameter):
    numbers = range(parameter)
    return '\n'.join(str(num) for num in numbers) + '\n'

@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1, operation, num2):
    operations = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        'div': lambda x, y: x / y,
        '%': lambda x, y: x % y
    }
    
    if operation not in operations:
        return "Invalid operation"
        
    result = operations[operation](num1, num2)
    return str(result)

if __name__ == '__main__':
    app.run(port=5555, debug=True)
