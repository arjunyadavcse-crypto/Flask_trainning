from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/calculator', methods=['POST', 'GET'])
def calculator():
    if request.method == 'GET':
        return render_template('calculator.html', ans='')

    try:
        a = float(request.form['a'])
        b = float(request.form['b'])
    except ValueError:
        return render_template('calculator.html', ans='Enter valid numbers')

    action = request.form['action']

    if action == '+':
        ans = a + b
    elif action == '-':
        ans = a - b
    elif action == '*':
        ans = a * b
    elif action == '/':
        ans = "Cannot divide by zero" if b == 0 else a / b
    else:
        ans = "Invalid operator"

    return render_template('calculator.html', ans=ans)


if __name__ == '__main__':
    app.run(debug=True)