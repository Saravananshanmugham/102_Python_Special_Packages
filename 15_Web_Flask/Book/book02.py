from flask import Flask, request
app = Flask(__name__)

@app.route("/")
def index():
    user_agent = request.headers.get('endpoint')
    return '<p> Your Brownwer is {}</p>'.format(user_agent)


if __name__==('__main__'):
    app.run(debug=True)