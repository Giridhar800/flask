from wtforms import *


class ContactForm(Form):
    Name = StringField('Candidate Name',[validators.data_required('please enter your name..')])
    Gender = RadioField('Gender', choices=[('M','Male'),('F','Female')])
    Address = TextAreaField("Address")
    email = StringField('Email',[validators.data_required("please enter email address"),validators.Email("please enter email address")])
    Age = IntegerField('Age')
    language = SelectField('Programming Languages', choices=[('c','c'),('py','python')])
    submit = SubmitField("submit")