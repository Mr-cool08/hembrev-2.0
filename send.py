import smtplib
from encrpyt import *
import datetime  
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders
import configparser
dt = datetime.date.today()
wk = dt.isocalendar()[1]





def sendmail():
    decrypt()
    config = configparser.ConfigParser()
    config.read('config.ini')
    mail1 = config.get('Emails', 'email1')
    mail2 = config.get('Emails', 'email2')
    mail3 = config.get('Emails', 'Email3')
    mail4 = config.get('Emails', 'Email4')
    mail5 = config.get('Emails', 'Email5')
    mail = config.get('login', 'email')
    with open('password.txt','r') as file:
        password = file.read()


    docname = 'hembrev v' + str(wk) + ".docx"
    msg = MIMEMultipart()
    msg['From'] = mail
## vilka som ska få mailet
    receivers = [mail1, mail2, mail3, mail4, mail5]
    msg['To'] = ', '.join(receivers)
    msg['Subject'] = 'hembrev v' + str(wk)
    body = 'hembrev v' + str(wk)
    msg.attach(MIMEText(body, 'plain'))

## ATTACHMENT PART OF THE CODE IS HERE
    attachment = open(docname, 'rb')
    part = MIMEBase('application', "octet-stream")
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % docname)
    msg.attach(part)

# construct the email item object
    server = smtplib.SMTP('smtp.office365.com', 587)  ### put your relevant SMTP here
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(mail, password)  ### if applicable
    server.send_message(msg)
    server.quit()
    encrypt()
    
    




