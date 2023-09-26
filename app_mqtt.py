import ssl
import sys
import time
import task_mqtt

from Adafruit_IO import MQTTClient
import view
from scheduler import *

scheduler = Scheduler()
scheduler.SCH_Init()

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

app = view.AppTkinter('IoT Application')

AIO_FEED_IDs = ["temperature_sensor"]
AIO_USERNAME = "HuyTran1996"
AIO_KEY = "aio_WwIl33pT8UUxhn18Ex4Cb8MLFETd"

task_mqtt = task_mqtt.TaskMQTT(tkinter_app=app)

scheduler.SCH_Add_Task(task_mqtt.TaskMQTT_Run, 1000, 2000)


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
    if feed_id == 'temperature_sensor':
        task_mqtt.set_value(temperature_arg=payload)


client = MQTTClient(AIO_USERNAME, AIO_KEY)
client.on_connect = connected
client.on_disconnect = disconnected
client.on_message = message
client.on_subscribe = subscribe
client.connect()
client.loop_background()

while True:
    scheduler.SCH_Update()
    scheduler.SCH_Dispatch_Tasks()
    app.run_app_update()
    time.sleep(0.1)
