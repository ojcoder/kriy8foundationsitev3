# from flask_wtf import FlaskForm
# from wtforms import TextField, TextAreaField, SubmitField, validators, ValidationError

# class ContactForm(FlaskForm):
# 	#addiding validators for user data
# 	name = TextField("Name",[validators.DataRequired("Please enter your name")])
# 	#make sure user enters an email
# 	email = TextField("Email", [validators.DataRequired("Please enter your email address"), validators.Email()])
# 	subject = TextField("Subject", [validators.DataRequired("Please enter a subject")])
# 	message = TextAreaField("Message", [validators.DataRequired("Please enter a message")])
# 	send = SubmitField("Send")

from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField, TextField
from wtforms import ValidationError, validators

class ContactForm(FlaskForm):
	name = TextField("Name", [validators.Required('Please enter your name !')])
	email = TextField("Email", [validators.Required('Please enter you email address !'), validators.Email()])
	subject = TextField("Subject", [validators.Required('Please enter a Subject !')])
	message = TextAreaField("Message", [validators.Required('Enter a message !')])
	send = SubmitField("Under Construction.")