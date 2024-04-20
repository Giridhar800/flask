from flask import *

app = Flask(__name__)
@app.route('/func/<int:num>')
def func(num):
    return render_template('index.html',n=num)


if __name__ == '__main__':
    app.run()