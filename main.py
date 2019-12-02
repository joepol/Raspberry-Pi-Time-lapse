import os
import sys
import time
from datetime import date, datetime
import logging

import capture
import gif_generator
import mail_sender

LOW_CAPTURE_RATE = 300  # seconds
HIGH_CAPTURE_RATE = 60

logging.basicConfig(filename='timelapse.log', level=logging.INFO, filemode='w', format='%(asctime)s %(name)s - %('
                                                                   'levelname)s - %(message)s')
logger = logging.getLogger('logger')
logger.setLevel(logging.INFO)
console = logging.StreamHandler()
console.setLevel(logging.INFO)

def get_hour_24():
    return int(datetime.now().strftime("%H"))


def is_time_to_send_gif():
    return get_hour_24() >= 10


def is_high_rate(hour):
    return 15 < hour < 18


is_gif_sent = False
# at 21 - pack images to a GIF
# mail daily GIF

# access_rights = 0o755

logging.info('Started time lapse at %s', datetime.now())

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

    #        Capture image
    # TODO : what about shutdown and restart opencv?
    directory_path = directory #+ '\\'
    capture.capture(directory_path)

    #         Go to sleep
    if is_high_rate(get_hour_24()):
        time.sleep(HIGH_CAPTURE_RATE)
    else:
        print("keepAlive : capturing images at low rate, num of frames {}".format(str(len(os.listdir(directory)))))
        time.sleep(LOW_CAPTURE_RATE)

    #       Generate GIF and mail it
    # TODO : use schedule library instead
    if not is_gif_sent and is_time_to_send_gif():
        file = gif_generator.generate_gif(directory)
        mail_sender.main(file)
        is_gif_sent = True
#         will now continue to capture images, not all will be GIF'ed

# TODO : when exit is called - relesase camera and create another GIF with the frames that were collected
