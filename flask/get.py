from flask import * 

app = Flask(__name__)

@app.route('/login1',methods=['GET'])
def login():
    username = request.args.get('username')
    password = request.args.get('password')
    if username == 'giri' and password == 'giri':
        return "wellcome %s" % username

if __name__ == '__main__':
    app.run()