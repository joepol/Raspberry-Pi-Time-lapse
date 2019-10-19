import smtplib
import ssl
import json
import sys

DEFAULT_MESSAGE = """\
Subject: Timelapse GIF

This message contain an animated GIF of last 24H time lapse."""


class MailSender:
    def __init__(self):
        # load mailing data
        with open('data.txt', 'r') as json_file:
            data = json.load(json_file)
            self.sender_mail = data['sender_mail']
            self.sender_password = data['sender_password']
            self.receipents_mails = data['receipents']  # a list of email addresses

    def send_mail(self, message=DEFAULT_MESSAGE):
        port = 465  # most be this port for SSL
        smtp_server = "smtp.gmail.com"

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(host=smtp_server, port=port, context=context) as server:
            server.login(self.sender_mail, self.sender_password)
            for receipent_mail in self.receipents_mails:
                try:
                    server.sendmail(self.sender_mail, receipent_mail, message)
                except:
                    print("Failed to send mail")


if __name__ == '__main__':
    sender = MailSender()
    if len(sys.argv) > 1:
        specific_message = sys.argv[1]
        sender.send_mail(message=specific_message)
    else:
        sender.send_mail()
