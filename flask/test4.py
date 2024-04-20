from flask import *

app = Flask(__name__)
@app.route('/')
def set_cookie():
    response = make_response("<h1> cookie is set</h1>")
    response.set_cookie('name',"giridhar")
    return response

if __name__ == "__main__":
    app.run()