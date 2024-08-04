from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome To Flask"

@app.route("/index")
def index():
    return "Welcome to Index Page"

@app.route("/userform", methods = ['POST', 'GET'])
def userform():
    if request.method =='POST':
        fname = request.form['fname']
        lname = request.form['lname']
        return fname +" "+lname
    return render_template('userform.html')

@app.route("/submitform", methods = ['POST', 'GET'])
def submitform():
    if request.method =='POST':
        fname = request.form['fname']
        lname = request.form['lname']
        return fname +" "+lname
    return render_template('userform.html')


if __name__ == "__main__":
    app.run(debug=True, port=8000)