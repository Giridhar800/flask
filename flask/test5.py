from flask import *

app = Flask(__name__)
app.secret_key = 'giri'
@app.route('/')
def home():
    response = make_response("<h3> session variable is set, <a href='/get'>Get variable</a></h3>")
    session['key']='hyderabad'
    return response

@app.route('/get')
def get_session():
    if 'key' in session:
        s = session['key']
        return render_template('getsession.html',name=s)
    
if __name__ == '__main__':
    app.run()