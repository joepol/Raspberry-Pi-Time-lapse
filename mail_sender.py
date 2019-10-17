import smtplib
import ssl
import json

port = 465  # most be this port for SSL
smtp_server = "smtp.gmail.com"

with open('data.txt', 'r') as json_file:
    data = json.load(json_file)
    sender_mail = data['sender_mail']
    sender_password = data['sender_password']
    receipents_mails = data['receipents'] # a list of email addresses

message = """\
Subject: Timelapse GIF

This message contain an animated GIF of last 24H time lapse."""

print("sender_mail is {}".format(sender_mail))

context = ssl.create_default_context()
with smtplib.SMTP_SSL(host=smtp_server, port=port, context=context) as server:
    server.login(sender_mail, sender_password)
    for receipent_mail in receipents_mails:
        server.sendmail(sender_mail, receipent_mail, message)
