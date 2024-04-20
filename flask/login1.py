from flask import *

app = Flask(__name__)
app.secret_key = "sycho"

@app.route('/')
def home():
    return render_template('home1.html')

@app.route('/login')
def login():
    return render_template('login3.html')

@app.route('/success',methods=['POST'])
def success():
    if request.method == 'POST':
        session['email'] = request.form['email']
    return render_template('success1.html')

@app.route('/logout')
def logout():
    if 'email' in session:
        session.pop('email',None)
        return render_template('logout.html')
    else:
        return '<p> User alredy logged out </p>'

@app.route('/profile')
def profile():
    if 'email' in session:
        email = session['email']
        return render_template('profile1.html',name=email)
    else:
        return '<p> Please login first</p>'
    
if __name__ == '__main__':
    app.run()
     

