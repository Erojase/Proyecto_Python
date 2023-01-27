import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


mail_content = "Buenas tardes"

sender_address = 'eduardo.rojas.sanchez@alumnojoyfe.iepgroup.es'

def sendTestMail():
    cwd = os.getcwd()
    with open("src/services/mail/auth_mail.txt", "r") as f:
        sender_pass = f.read()

    with open("src/services/mail/correo.txt", "r") as f:
        receiver_address = f.read()

    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = 'Correo de pagina web'
    
    message.attach(MIMEText(mail_content, 'plain'))
    
    session = smtplib.SMTP('smtp.gmail.com', 587)
    session.starttls()
    session.login(sender_address, sender_pass)
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()
    print('Mail Sent')