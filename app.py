from flask import Flask, render_template, request, flash, redirect, url_for
from forms import ContactForm
from flask_mail import Message, Mail

app = Flask(__name__)

#load development configuration
app.config.from_pyfile('development.py')

#load production configuration 
# app.config.from_pyfile('production.py')


#set up mail
mail = Mail()
# app.debug = 0 
mail.init_app(app)

#During testing, this function needs to be commented out since the Flask development server users HTTP
#When in production, you want to uncomment this function to redirect all calls to HTTPS
#to force all requests to HTTPS
# @app.before_request
# def before_request():
# 	if request.url.startswith('http://'):
# 		url = request.url.replace('http://', 'https://',1)
# 		code = 301
# 		return redirect(url, code = code)

#@app.route("/", methods=['GET'])
@app.route("/", methods=['GET'])
def home():
	return render_template('home.html', title='Kriy8 Foundation', nav='home')





@app.route("/about/")
def about():
	return render_template('about.html', title='About Us')

@app.route("/resources/")
def resources():
	return render_template('resources.html', title='Resources')

@app.route("/resources/healthyfuture")
def healthyfuture():
	return render_template('healthyfuture.html', title='Tips for a Healthy Future')
@app.route("/resources/antibiotics")
def antibiotics():
	return render_template('antibiotics.html', title='Antibiotic Resistance')
@app.route("/resources/organdonation")
def organdonation():
	return render_template('organdonation.html', title='Organ Donation')

@app.route("/podcast/")
def podcast():
	return render_template('podcast.html', title='Podcast')
@app.route("/testimonials/")
def testimonials():
	return render_template('testimonials.html', title='Testimonials')


@app.route("/donation/")
def donation():
	return render_template('donation.html', title='Donation')

@app.route("/associates/")
def associates():
	return render_template('associates.html', title='Associates')

@app.route("/contact/", methods=['GET', 'POST'])
def contact():
	form = ContactForm(request.form)
	#obtaining data from forms 
	if request.method == 'POST':
		name = request.form['name']
		email = request.form['email']
		subject = request.form['subject']
		message = request.form['message']
		#if all the data has been entered and is valid, then send email
		if form.validate_on_submit():
			flash(f"Thank you for your message. We'll get back to you soon", "success")

			msg = Message(form.subject.data, sender='project20team@gmail.com', recipients=['project20team@gmail.com'])
			msg.body = """
			From: {} <{}>
			{}

			""".format(form.name.data, form.email.data, form.message.data)
			#mail.send(msg)
			#we were able to send the email
			#and redirect user to the contact page again
			return redirect(url_for('contact'))
		return render_template('contact.html', title='Contact Us', form = form )
			
	elif request.method == 'GET':
		return render_template('contact.html', title='Contact Us', form = form )

#not found route 
@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html', title="Not Found"), 404


if __name__ == '__main__':
	app.run()





