import sys

import requests
# //run command to fix ssl error
# ln -s /etc/ssl/* /Library/Frameworks/Python.framework/Versions/3.9/etc/openssl
from Adafruit_IO import MQTTClient
import time
import random
import constants
import sensor_feeds
# import camera_detector
# import cv2
import eval_testing

AIO_FEED_IDs = ["equation"]
AIO_USERNAME = "HuyTran1996"
AIO_KEY = "aio_RIWu45IS3Gsy8RnaGbnJhepme3n7"
import base64
import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

# camera_detect_model = camera_detector.CameraDetector()


def init_latest_equation():
    aio_url = 'https://io.adafruit.com/api/v2/HuyTran1996/feeds/equation'
    x = requests.get(url=aio_url, headers={'Authorization': AIO_KEY})
    return x.json()['last_value']


equation = init_latest_equation()

equationManager = eval_testing.EvalEquation(equation)


def connected(client):
    print("Ket noi thanh cong ...")
    for topic in AIO_FEED_IDs:
        client.subscribe(topic)


def subscribe(client, userdata, mid, granted_qos):
    print("Subscribe thanh cong ...")


def disconnected(client):
    print("Ngat ket noi ...")
    sys.exit(1)


def message(client, feed_id, payload):
    print("Nhan du lieu: " + payload + ", feed id:" + feed_id)
    if feed_id == 'equation':
        equationManager.set_equation(payload)
        print('update equation')


client = MQTTClient(AIO_USERNAME, AIO_KEY)
client.on_connect = connected
client.on_disconnect = disconnected
client.on_message = message
client.on_subscribe = subscribe
client.connect()
client.loop_background()


def publish_data_to_feed():
    print("random data temperature")
    temp = random.randint(constants.MIN_TEMPERATURE, constants.MAX_TEMPERATURE)
    client.publish(sensor_feeds.TEMPERATURE_SENSOR_FEED_NAME, temp)

    print("random data humidity")
    humidity = random.randint(constants.MIN_HUMIDITY, constants.MAX_HUMIDITY)
    client.publish(sensor_feeds.HUMIDITY_SENSOR_FEED_NAME, humidity)

    print("random data light")
    light = random.randint(constants.MIN_LIGHT, constants.MAX_LIGHT)
    client.publish(sensor_feeds.LIGHT_SENSOR_FEED_NAME, light)


# def scale_image_1024(image):
#     image = cv2.resize(image, (100, 100), interpolation=cv2.INTER_AREA)
#     quality = 90  # You can adjust this value (0-100)
#     _, encoded_image = cv2.imencode('.jpg', image, [int(cv2.IMWRITE_JPEG_QUALITY), quality])
#
#     # Check the file size
#     file_size = len(encoded_image.tobytes())
#     target_size = 1024  # Target file size in bytes
#     while file_size > target_size and quality > 0:
#         quality -= 10
#         _, encoded_image = cv2.imencode('.jpg', image, [int(cv2.IMWRITE_JPEG_QUALITY), quality])
#         file_size = len(encoded_image.tobytes())
#     file_size = len(encoded_image.tobytes())
#     print(file_size)
#     return encoded_image


# def image_to_string256(image):
#     ret, buffer = cv2.imencode('.jpg', image)
#     image_as_bytes = buffer.tobytes()
#     image_as_base64 = base64.b64encode(image_as_bytes).decode()
#     return image_as_base64


counter = 0
while True:
    print('cong thuc equation: {}'.format(equationManager.equation))
    x1 = random.randint(1, 10)
    x2 = random.randint(1, 10)
    x3 = random.randint(1, 10)
    print({'x1': x1, 'x2': x2, 'x3': x3})
    result = equationManager.cal_eval(x1, x2, x3)
    print(result)
    client.publish(sensor_feeds.EQUATION_FEED, result)
    time.sleep(5)
    pass
