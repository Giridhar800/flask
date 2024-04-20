from flask import *

app=Flask(__name__)

@app.route('/login',methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    if username == 'giri' and password == 'giri':
        return "wellcome %s" % username
    else:
        return "Invallid username or password"
    
if __name__ == '__main__':
    app.run()