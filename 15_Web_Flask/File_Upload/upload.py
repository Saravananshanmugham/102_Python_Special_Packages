from flask import *  
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)  
app.config['UPLOAD_FOLDER']="C:/MyLearn/ML_AI_DS/90_Special_Packages/05_Package_Flask/File_Upload/Upload/"
 
@app.route('/')  
def upload():  
    return render_template("file_upload_form.html")  
 
@app.route('/success', methods = ['POST'])  
def success():  
    if request.method == 'POST':  
        f = request.files['file']  
        base_path = os.path.abspath(os.path.dirname(__file__))
        upload_path = os.path.join(base_path, app.config['UPLOAD_FOLDER'])
        f.save(os.path.join(upload_path, secure_filename(f.filename)))
        #f.save(f.filename)  
        return render_template("fsuccess.html", name = f.filename)  
  
if __name__ == '__main__':  
    app.run(debug = True)  