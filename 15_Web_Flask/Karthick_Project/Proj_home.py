from flask import *  
import sqlite3

app = Flask(__name__) 
app.secret_key = "abc"  
 
@app.route('/')  
def home():  
    return render_template("index.html")  

@app.route('/signup')  
def signup():  
    return render_template("signup.html")  

@app.route("/savedetails",methods = ["POST","GET"])  
def saveDetails():  
    msg = "msg"  
    if request.method == "POST":  
        try:  
            enr_no = request.form["Enr_no"]
            uname = request.form["uname"]  
            passwd = request.form["passwd"]  
            with sqlite3.connect("IR40.db") as con:  
                cur = con.cursor()  
                
                insert_query="""INSERT into student_record 
                (Enr_no, Stud_name, passwd) 
                values 
                (?,?,?)"""

                cur.execute(insert_query,(enr_no,uname,passwd))  
                con.commit()  
                msg = "Student successfully Added"  
        except:  
            con.rollback()  
            msg = "We can not add the Student to the list"  
        finally:  
            return render_template("message.html",msg = msg)  
            con.close()  
 
@app.route("/login",methods = ["POST","GET"])  
def login():  
    if request.method == "POST":  
        try:  
            Enr_no = request.form["Enr_no"]
            passwd=request.form["passwd"]
            
            with sqlite3.connect("IR40.db") as con:  
                con.row_factory = sqlite3.Row 
                cur = con.cursor()  
                sql_query="select * from student_record where Enr_no=?"
                cur.execute(sql_query,(Enr_no,))  
                rows = cur.fetchall()
                for row in rows:
                    if row["passwd"] == passwd:
                        session['Enr_no']=Enr_no
                        session["Username"]=row["Stud_name"]
                        return render_template("menu.html", msg=row["Stud_name"])
                    else:
                        return render_template("message.html", msg="Password Does Not Match")
        except:  
            msg = "can't be Selected"   
              

@app.route("/menu")
def menu_display():
    s = session['Username']
    return render_template("menu.html", msg=s)


@app.route("/view")
def view():
    con = sqlite3.connect("IR40.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    sql_query = "select * from student_record"
    cur.execute(sql_query)
    rows = cur.fetchall()
    msg = type(rows)
    return render_template("view.html", rows=rows, msg=msg)
  
if __name__ == '__main__':  
    app.run(debug = True) 