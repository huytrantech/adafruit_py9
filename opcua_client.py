import time

from opcua import Client

url = "opc.tcp://192.168.233.1:4200"

client = Client(url)

client.connect()
print("client connected")

while True:
    Temp = client.get_node("ns=2;i=2")
    Temperature = Temp.get_value()
    print(Temperature)

    Press = client.get_node("ns=2;i=3")
    Pressure = Press.get_value()
    print(Pressure)

    TimeV = client.get_node("ns=2;i=4")
    TimeVAlue = TimeV.get_value()
    print(TimeVAlue)
    time.sleep(1)