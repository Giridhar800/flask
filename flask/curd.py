from flask import *
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index2.html')

@app.route('/add')
def add():
    return render_template('add.html')

@app.route('/savedetails',methods=['POST','GET'])
def saveDetails():
    msg = "msg"
    if request.method == "POST":
        try:
            name = request.form['name']
            email = request.form['email']
            address = request.form['address']
            with sqlite3.connect('student.db') as con:
                cur = con.cursor()
                cur.execute("INSERT into Students (name, email, address) values (?,?,?)",(name,email,address))
                con.commit()
                msg = "student successfully Added"
        except:
            con.rollback()
            msg = "We can not add the student to the list"
        finally:
            return render_template('success3.html',msg=msg)
            con.close()

@app.route('/view')
def view():
    con = sqlite3.connect('student.db')
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("select * from Students")
    rows = cur.fetchall()
    return render_template('view.html',rows=rows)

@app.route('/delete')
def delete():
    return render_template('delete.html')

@app.route('/deleterecord',methods=['POST'])
def deleterecord():
    id = request.form['id']
    with sqlite3.connect('student.db') as con:
        try:
            cur = con.cursor()
            cur.execute("delete from Students where id = ?", id)
            msg = "record successfuly deleted"
        except:
            msg = "can't be deleted"
        finally:
            return render_template('deleterecord.html',msg=msg)
        
if __name__ == '__main__':
    app.run()
    