from email.mime.multipart import MIMEMultipart
from multiprocessing import context
import smtplib, ssl
from email.mime.text import MIMEText

C = ''
R = ''

context = ssl.create_default_context()

message = MIMEMultipart('alternative')
message['subject'] = 'prueba'
message['from'] = C
message['To'] = R

H = """

        <html>
            <head>
            <head/>
            <body>
            <h1>Hola Mundo<h1/>
            <body/>
        <html/>

"""
A =  MIMEText(H, 'html')

message.attach(A)

E = smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context)

E.ehlo()
E.login('', '')
E.sendmail(C, R, A.as_string())
E.quit()
