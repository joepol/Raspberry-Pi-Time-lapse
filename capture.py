import cv2
import time
import logging

DEFAULT_PATH = 'temp\\'

logger = logging.getLogger(__name__)


camera_port = 0
camera = cv2.VideoCapture(camera_port)
if not camera.isOpened():
    logger.critical()
    raise Exception("Could not open video device")


def capture(path=DEFAULT_PATH):
    # TODO: sanitize input!
    # camera.set(cv2.CAP_PROP_FRAME_WIDTH, 160)
    # camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 120)
    return_value, image = camera.read()
    image_file_name = path+ "/" + "{}.jpeg".format(int(time.time()))
    cv2.imwrite(image_file_name, image)
    logger.info("Image captured and saved by the name %s", image_file_name)


def shutdown():
    camera.release()
    cv2.destroyAllWindows()
