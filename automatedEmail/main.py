import datetime as dt
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import random
import smtplib
from userpass import UserPass

# smtp_user = 'testyams1@gmail.com'
# smtp_password = 'ulgegtorjailvwum' # App password
server = 'smtp.gmail.com'
port = 587 # Port 587 is used for email submission, supports SSL and TSL use

# MIME: multipurpose internet email extentions

user = UserPass(email = "testyams1@gmail.com", password = 'ulgegtorjailvwum')

def send_email(subject, body, sender, recepients):
    msg = MIMEMultipart("alternative")
    msg["Subject"] = subject
    msg["From"] = sender
    msg["To"] = recepients
    msg.attach(MIMEText('\n'+ body, 'plain'))

    with smtplib.SMTP(server, port) as s:
        s.ehlo()
        s.starttls() # encrypts email message, TLS means transport layer security
        s.login(user.email, user.password) # logs into email
        s.sendmail(from_addr=user.email, to_addrs="yamlakdshim@gmail.com", msg=msg.as_string())
    print('Sending Message...')
    print('Message Sent!')

def mondayMotivation():
    with open('quotes.txt') as quotes:
        quotesList = []
        for line in quotes:
            quotesList.append(line)
    send_email(subject = input('Subject: '), body = random.choice(quotesList), sender = input("Your email: "), recepients= input('Sending To: '))



day = dt.datetime.now()
if day.weekday() == 0:
    mondayMotivation()
else:
    send_email(subject = input('Subject: '), body = input('Message: '), sender = input("Your email: "), recepients= input('Sending To: '))



