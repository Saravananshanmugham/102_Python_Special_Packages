from flask import *
app=Flask(__name__)

@app.route("/")
def home():
    str = """
    <html>
        <body>
            <h1> Hi, Welcome to My Website</h1>
            <h2> This is Header 2</h2>
            <h3> This is Header 3</h3>
        </body>
    </html>
    """
    return str

'''
Rendering External HTML File
Flask facilitates us to render the external HTML file instead 
of hardcoding the HTML in the view function. 

Here, we can take advantage of the jinja2 template engine 
on which the flask is based.

Flask provides us the render_template() function 
which can be used to render the external HTML file 
to be returned as the response from the view function.

we must create the folder templates inside the 
application directory and save the HTML 
templates referenced in the flask script in that directory.
'''

@app.route("/template")
def message():
    return render_template('message.html')
 
'''
Rendering template with Delimiters 
{{ ... }} for expressions to print to the template output
'''
@app.route('/user/<uname>')  
def message1(uname):  
      return render_template('message_delimiter.html',name=uname)


'''
Embedding Python statements in HTML
Due to the fact that HTML is a mark-up language and purely used 
for the designing purpose, sometimes, in the web applications, 
we may need to execute the statements for the 
general-purpose computations. 

For this purpose, Flask facilitates us the delimiter {%...%} 
which can be used to embed the simple python statements into the HTML.
'''

@app.route('/table/<int:num>')  
def table(num):  
      return render_template('print_tables.html',n=num) 


'''
Referring Static files in HTML
------------------------------

The static files such as CSS or JavaScript file enhance the 
display of an HTML web page. A web server is configured to 
serve such files from the static folder in the package or 
the next to the module. The static files are available at the 
path /static of the application.

CSS
The flask template system finds the static CSS file under 
static/css directory. 

Hence the style.css is saved at the specified path.
'''
@app.route('/css')  
def message3():  
      return render_template('message_css.html') 

if __name__ == '__mnin__':
    app.run(debug=True)