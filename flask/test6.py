from flask import *

app = Flask(__name__)
app.secret_key = 'abc'

@app.route('/index1')
def home():
    return render_template("index1.html")

@app.route('/login', methods=['GET','POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['password'] != 'giri':
            error = "invallid password"
        else:
            flash("you are successfuly logged in")
            return redirect(url_for('home'))
    return render_template('login4.html',error=error)

if __name__ == '__main__':
    app.run()