from flask import *

app=Flask(__name__)
@app.route('/admin')
def admin():
    return 'admin page'

@app.route('/employee')
def employee():
    return 'employee page'

@app.route('/student')
def student():
    return 'student page'

@app.route('/user/<name>')
def user(name):
    if name == 'admin':
        return redirect(url_for('admin'))
    if name =='employee':
        return redirect(url_for('student'))
    if name == 'student':
        return redirect(url_for('student'))
    
if __name__=='__main__':
    app.run()
    
