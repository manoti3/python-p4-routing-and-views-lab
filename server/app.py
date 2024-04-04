# #!/usr/bin/env python3

# from flask import Flask

# app = Flask(__name__)

# @app.route('/')
# def index():
#     return '<h1>Python Operations with Flask Routing and Views</h1>'

# @app.route('/print/<parameter>')
# def print_parameter(parameter):
#     print(parameter)
#     return f'{parameter}'

# @app.route('/count/<parameter>')
# def count_parameter(parameter):
#     response = ''
#     for i in range(int(parameter)):
#         response += f'{i}\n'
#     return response

# @app.route('/math/<int:num1><operation><int:num2>')
# def math_parameters(num1, operation, num2):
#     print(num1)
#     print(operation)
#     if operation == '+':
#         return f'{int(num1) + int(num2)}'
#     elif operation == '-':
#         return f'{int(num1) - int(num2)}'
#     elif operation == '*':
#         return f'{int(num1) * int(num2)}'
#     elif operation == 'div':
#         return str(int(num1) / int(num2))
#     elif operation == '%':
#         return str(int(num1) % int(num2))

# if __name__ == '__main__':
#     app.run(port=5555, debug=True)

#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<parameter>')
def print_parameter(parameter):
    print(parameter)
    return parameter

@app.route('/count/<int:number>')
def count_parameter(number):
    response = ''
    for i in range(number):
        response += f'{i}\n'
    return response

@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math_parameters(num1, operation, num2):
    if operation == '+':
        return str(num1 + num2)
    elif operation == '-':
        return str(num1 - num2)
    elif operation == '*':
        return str(num1 * num2)
    elif operation == 'div':
        if num2 == 0:
            return "Error: Division by zero"
        else:
            return str(num1 / num2)
    elif operation == '%':
        return str(num1 % num2)
    else:
        return "Invalid operation"

if __name__ == '__main__':
    app.run(port=5555, debug=True)
