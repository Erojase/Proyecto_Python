from src.services.dbManager import *
import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv

load_dotenv()

TEST_BODY = "Buenas tardes"
SENDER = os.environ.get("MAIL")
PASSWD = os.environ.get("PASS")

def sendTestMail():
    
    reciever_address = SENDER

    message = MIMEMultipart()
    message['From'] = SENDER
    message['To'] = reciever_address
    message['Subject'] = 'Correo de prueba'
    
    message.attach(MIMEText(TEST_BODY, 'plain'))
    
    session = smtplib.SMTP('smtp.gmail.com', 587)
    session.starttls()
    session.login(SENDER, PASSWD)
    text = message.as_string()
    session.sendmail(SENDER, reciever_address, text)
    session.quit()
    print('Mail Sent')
    return "Mail Sent"

def sendTo(reciever:str, subject:str, body:str):

    msg = MIMEMultipart()
    msg['From'] = SENDER
    msg['To'] = reciever
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    # attachment = open(filepath, 'rb')

    # p = MIMEBase('application', 'octet-stream')
    # p.set_payload(attachment.read())
    # encoders.encode_base64(p)
    # p.add_header('Content-Disposition', "attachment; filename= %s" % filename)

    # msg.attach(p)

    s = smtplib.SMTP('smtp.gmail.com', 587)  # SMTP
    s.starttls()
    s.login(SENDER, PASSWD)

    text = msg.as_string()

    s.sendmail(SENDER, reciever, text)
    # status = s.getreply()
    s.quit()
    print("Finished")
    # return status
    
def broadcast(subject:str, body:str):
    '''
    Function that allows a broadcast to every user in the database
    ''' 
    db:DbManager = DbManager()
    
    mails = []
    
    users = db.listUsers()
    for user in users:
        mails.append(user['mail'])
        
    
    return "Not yet implemented"