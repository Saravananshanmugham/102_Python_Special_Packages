from flask import Flask, redirect, url_for
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, Saravanan"

@app.route("/home")
def home():
    return "This is home page URL"

@app.route("/home/<name>")
def home1(name):
    return "Welcome "+ name

@app.route("/home/<int:age>")
def home2(age):
    return "My Age is %d"%age

'''
The add_url_rule() function
There is one more approach to perform routing for the flask web application that can be done by using the add_url() function of the Flask class. The syntax to use this function is given below.
```python
add_url_rule(<url rule>, <endpoint>, <view function>)  ```

This function is mainly used in the case if the view function is not given and we need to connect a view function to an endpoint externally by using this function.
'''

def about1():  
    return "This is about page";  
  
app.add_url_rule("/about","about2",about1)

''' URL Binding'''
@app.route("/adminp")
def admin_p():
    return 'Admin Portal'

@app.route("/Student")
def student():
    return 'Student Portal'

@app.route("/user/<name1>")
def user(name1):
    if name1=='admin':
        return redirect(url_for('admin_p'))
    
    if name1=='Student':
        return redirect(url_for('student'))
    

if __name__ == '__main__':
    app.run(debug=True, port=5010)