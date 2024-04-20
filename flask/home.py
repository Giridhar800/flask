from flask import * 

app = Flask(__name__)
@app.route('/home/<name>')
def home(name):
    return render_template('home.html',name=name)

if __name__ == '__main__':
    app.run()