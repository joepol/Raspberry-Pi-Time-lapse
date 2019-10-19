import cv2
import time

camera_port = 0
camera = cv2.VideoCapture(camera_port, cv2.CAP_DSHOW)
if not camera.isOpened():
    raise Exception("Could not open video device")

# camera.set(cv2.CAP_PROP_FRAME_WIDTH, 160)
# camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 120)
# TODO : create a directory for each day (or any sampling period)
path = 'images\\'

for i in range(5):
    print("Capturing an image")
    return_value, image = camera.read()
    image_file_name = path + "{}.png".format(int(time.time()))
    cv2.imwrite(image_file_name, image)
    time.sleep(1)
    print("Image captured and saved by the name {}".format(image_file_name))

camera.release()
cv2.destroyAllWindows()
