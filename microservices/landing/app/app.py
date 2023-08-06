from flask import Flask, render_template, request, flash, redirect, url_for
import requests
import os

app = Flask(__name__)
app.secret_key = 'thisisjustarandomstring'

# Updated API endpoints
ADD_API_ENDPOINT = 'http://addition:5051'
SUB_API_ENDPOINT = 'http://subtraction:5052'
MUL_API_ENDPOINT = 'http://multiplication:5053'
DIV_API_ENDPOINT = 'http://division:5054'
MOD_API_ENDPOINT = 'http://modulus:5055'
EXP_API_ENDPOINT = 'http://exponent:5056'
GCD_API_ENDPOINT = 'http://gcd:5057'


@app.route('/', methods=['POST', 'GET'])
def index():
    number_1 = request.form.get("first")
    number_2 = request.form.get('second')
    operation = request.form.get('operation')
    result = 0

    if number_1 is None or number_2 is None:
        flash('Please enter both numbers')
    elif not number_1.isnumeric() or not number_2.isnumeric():
        flash('Please enter valid numbers')
    elif operation == 'add':
        response = requests.get(f'{ADD_API_ENDPOINT}/{number_1}/{number_2}')
        result = response.json()['result']
    elif operation == 'minus':
        response = requests.get(f'{SUB_API_ENDPOINT}/{number_1}/{number_2}')
        result = response.json()['result']
    elif operation == 'multiply':
        response = requests.get(f'{MUL_API_ENDPOINT}/{number_1}/{number_2}')
        result = response.json()['result']
    elif operation == 'divide':
        if number_2 == '0':
            flash('Cannot divide by zero')
        else:
            response = requests.get(f'{DIV_API_ENDPOINT}/{number_1}/{number_2}')
            result = response.json()['result']
    elif operation == 'modulus':
        if number_2 == '0':
            flash('Cannot do modulus by zero')
        else:
            response = requests.get(f'{MOD_API_ENDPOINT}/{number_1}/{number_2}')
            result = response.json()['result']
    elif operation == 'exponent':
        response = requests.get(f'{EXP_API_ENDPOINT}/{number_1}/{number_2}')
        result = response.json()['result']
    elif operation == 'gcd':
        response = requests.get(f'{GCD_API_ENDPOINT}/{number_1}/{number_2}')
        result = response.json()['result']

    flash(f'The result of operation {operation} on {number_1} and {number_2} is {result}')

    return render_template('index.html')


if __name__ == '__main__':
    app.run(
        debug=True,
        port=5050,
        host="0.0.0.0"
    )
