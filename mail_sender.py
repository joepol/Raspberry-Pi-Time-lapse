import yagmail
import json
import sys
import logging

SUBJECT = "Timelapse GIF"


class MailSender:
    def __init__(self):
        # load mailing data
        with open('data.txt', 'r') as json_file:
            data = json.load(json_file)
            self.sender_mail = data['sender_mail']
            self.sender_password = data['sender_password']
            self.receipents_mails = data['receipents']  # a list of email addresses

    def send_mail(self, attachment_file_name):
        # TODO: add current date
        message_content = "This message contain an animated GIF of last 24H time lapse."

        yag = yagmail.SMTP(user=self.sender_mail, password=self.sender_password)
        for receipent_mail in self.receipents_mails:
            yag.send(
                to=receipent_mail,
                subject=SUBJECT,
                contents=message_content,
                attachments=attachment_file_name,  # should be in the format of timelapse_DD_MM_YYYY.gif
            )


def main(file_name):
    sender = MailSender()
    sender.send_mail(attachment_file_name=file_name)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        file_name = sys.argv[1]
        main(file_name)
    # TODO : else - log an error

main(file_name='images\\timelapse_25_10_2019.gif')
