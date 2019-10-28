import os
import sys
import time
from datetime import date, datetime
import logging

import capture
import gif_generator
import mail_sender

LOW_CAPTURE_RATE = 600  # seconds
HIGH_CAPTURE_RATE = 30

logging.basicConfig(filename='timelapse.log', filemode='w', format='%(asctime)s %(name)s - %('
                                                                   'levelname)s - %(message)s')


def get_hour_24():
    return int(datetime.now().strftime("%H"))


def is_time_to_send_gif():
    return get_hour_24() > 21


def is_high_rate(hour):
    return 15 < hour < 20


is_gif_sent = False
# at 21 - pack images to a GIF
# mail daily GIF

# access_rights = 0o755

logging.info('Started time lapse at')

while True:
    #       Create a daily dir
    today = date.today().strftime("%d_%m_%Y")  # dd/mm/YY
    directory = str(today)
    if not os.path.exists(directory):
        try:
            os.mkdir(directory)
            is_gif_sent = False
        except OSError:
            logging.critical("Creation of the directory {} failed".format(directory))
            sys.exit("Failed to create a directory")

    #         Go to sleep
    if is_high_rate(get_hour_24()):
        time.sleep(HIGH_CAPTURE_RATE)
    else:
        time.sleep(LOW_CAPTURE_RATE)

    #        Capture image
    capture.capture(directory)

    #       Generate GIF and mail it
    # TODO : use schedule library instead
    if not is_gif_sent and is_time_to_send_gif():
        file = gif_generator.generate_gif(directory)
        mail_sender.main(file)
        is_gif_sent = True
#         will now continue to capture images, not all will be GIF'ed
