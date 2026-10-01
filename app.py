from flask import Flask ,render_template, request, redirect, url_for
app = Flask(__name__)

@app.route('/')

def home():
    return "<h1>This is flask page</h1>"

@app.route('/welcome')

def welcome():
    return "<h1>Welcome to flask page</h1>"

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/success/<int:a>')
def success(a):
    return "The person is pass and the score is "+str(a)

@app.route('/fail/<float:a>')
def fail(a):
    return "The person is fail and the score is "+str(a)

@app.route('/calculate' , methods=['POST','GET'])

def calculate():
    if request.method=='GET':
        return render_template('calculate.html')
    else:
        maths = float(request.form['maths'])
        physics = float(request.form['physics'])
        chemistry = float(request.form['chemistry'])
        avg = (maths + physics + chemistry)/3
        result = ""
        if avg>80:
            result = "success"
        else:
            result = "fail"

    
    return redirect(url_for(result,a=avg))

if __name__== '__main__':
    app.run(debug=True)
