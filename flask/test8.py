from flask import Flask, render_template, request, flash 
from forms import ContactForm 
app = Flask(__name__) 
app.secret_key = 'development key' 

@app.route('/contact', methods=['GET', 'POST']) 
def contact(): 
    form = ContactForm() 
    if form.validate() == False: 
        print('All fields are required.') 
        return render_template('contact.html', form=form) 

@app.route('/success', methods=['GET', 'POST']) 
def success(): 
    return render_template("success4.html") 

if __name__ == '__main__': 
 app.run()

 