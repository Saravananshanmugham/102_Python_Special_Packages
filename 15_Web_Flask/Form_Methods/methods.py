from flask import Flask, request
app = Flask(__name__)

'''
POST Method
Form data is posted to server.
'''

@app.route("/login_post", methods=["POST"])
def login_post():
    username = request.form['uname']
    password = request.form['passwd']
    str = "<p>User Name is " + username+"<br> Password is "+password
    return str

'''
Get Method
Parameter are passed to the server in the URL
'''
@app.route("/login_get", methods=["GET"])
def login_get():
    username = request.args.get('uname')
    password = request.args.get('passwd')
    str = "<p>User Name is " + username+"<br> Password is "+password
    return str

if __name__=='__main__':
    app.run(debug=True)