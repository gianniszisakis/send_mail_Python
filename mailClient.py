import smtplib, ssl
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

port = 465 #SSL port connection for gmail
smtp_server = input("Give smtp server(e.g smtp.gmail.com): ")
sender_email = input("Sender email: ")
password = input("Password of your email: ")
receiver_email = input("Give the receiver email: ")
message = """\
Subject: Hello
Hello test python email message."""  #the message you want to deliver



context = ssl.create_default_context() 

######################## Send message code ###############################
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
	server.login(sender_email, password)
	server.sendmail(sender_email, receiver_email, message)
######################## Send message code ###############################

