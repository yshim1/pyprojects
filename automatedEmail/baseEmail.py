from abc import ABC, abstractmethod
import datetime as dt
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from userpass import UserPass


class AbstractBaseEmail(ABC):
    # smtp_user = 'testyams1@gmail.com'
    # smtp_password = 'ulgegtorjailvwum' # App password
    server = 'smtp.gmail.com'
    port = 587 # Port 587 is used for email submission, supports SSL and TSL use

    # MIME: multipurpose internet email extentions

    user = UserPass(email = "testyams1@gmail.com", password = 'ulgegtorjailvwum')
    @abstractmethod
    def __init__(self, subject, body, sender, recepients):
        pass
    
    @abstractmethod
    def send_email(self, subject, body, sender, recepients):
        msg = MIMEMultipart("alternative")
        msg["Subject"] = subject
        msg["From"] = sender
        msg["To"] = recepients
        msg.attach(MIMEText('\n'+ body, 'plain'))

        with smtplib.SMTP(self.server, self.port) as s:
            s.ehlo()
            s.starttls() # encrypts email message, TLS means transport layer security
            s.login(self.user.email, self.user.password) # logs into email
            s.sendmail(from_addr=self.user.email, to_addrs="yamlakdshim@gmail.com", msg=msg.as_string())

    def mondayMessage(self, subject, body, sender, recepients):
        pass


    send_email(subject = input('Subject: '), body = input('Message: '), sender = input("Your email: "), recepients= input('Sending To'))




