from flask import Flask

app=Flask(__name__)

def home():
    return "this is home page"
app.add_url_rule('/home',"home",home)

if __name__ == "__main__":
    app.run()