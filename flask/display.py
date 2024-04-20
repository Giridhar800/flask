from flask import * 


app = Flask(__name__) 
@app.route('/') 
def display(): 
 return "<h1>Hai, Welcome to Hyderabad</h1>" 


if __name__ == '__main__': 
 app.run()