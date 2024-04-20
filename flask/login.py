from flask import *

app = Flask(__name__)


@app.route('/error')
def error():
    return "<p><strong>Enter correct password</strong></p>"

@app.route('/')
def login():
    return render_template("login2.html")

@app.route('/success',methods=['POST'])
def success():
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']

    if password == "giri":
        response = make_response(render_template('success.html'))
        response.set_cookie('email',email)
        return response
    else:
        return redirect(url_for('error'))

@app.route('/viewprofile')
def profile():
    email = request.cookies.get('email')
    response = make_response(render_template('profile.html',name=email))
    return response

if __name__ == '__main__':
    app.run()