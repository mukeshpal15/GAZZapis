from .views import *
from django.core.mail import EmailMessage
from django.core.mail import BadHeaderError, send_mail


def sendmail(e,p):
	try:
		subject='Mail From GAAZ'
		msg= ''' Hello sir,

		your Password is'''+p+''' 

		Thanks & Regards
		Shri Raj Property''' 


		email = EmailMessage(subject, msg, to=[e])
		email.send()
		return 1
	except:
		return 0