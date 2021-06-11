import smtplib
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
import os

email_user = "abc@gmail.com"
email_password = "12345678"
from_email = "abc@gmail.com"
to_emails = ["efg@gmail.com"]
body = "Please see the attached video for more information about violation"
subject = "Alert for possible driver sleeping"
email_server = 'smtp.gmail.com'
email_server_port = 465

def send_mail(from_email, to_emails, subject, body, file, email_server):
    assert isinstance(to_emails, list)

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = COMMASPACE.join(to_emails)
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject

    msg.attach(MIMEText(body))

    with open(file, "rb") as fil:
        part = MIMEApplication(fil.read(), Name=basename(file))
    # After the file is closed
    part['Content-Disposition'] = 'attachment; filename="%s"' % basename(file)
    msg.attach(part)

    email_server.sendmail(from_email, to_emails, msg.as_string())
    print('Email sent!')


def email_server_login(email_user, email_password, server="smtp.gmail.com", port=465):
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(email_user, email_password)
    return server

def send(count):
    file_name = "cam_video"+str(count)+".mp4"
    email_server_connection = email_server_login(email_user, email_password, email_server, email_server_port)
    send_mail(from_email, to_emails, subject,body, file_name, email_server_connection)
    email_server_connection.close()
    os.remove(file_name)