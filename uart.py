import serial.tools.list_ports


class DeviceManager(object):

    def __init__(self,comm_port="None",baudrate=115200):
        self.comm_port = comm_port
        if comm_port == "None":
            self.comm_port = get_port()
        self.baudrate = baudrate
        self.ser = serial.Serial(port=self.comm_port, baudrate=self.baudrate)
        self.adafruit_io = None

    def add_adafruit_io(self,client_adafruit):
        self.adafruit_io = client_adafruit

    def write_data_to_device(self,data):
        self.ser.write(str(data).encode())
        pass

    def read_data_from_device(self):
        mess = ""
        if self.comm_port != "None" and self.adafruit_io is not None:
            bytes_to_read = self.ser.inWaiting()
            if bytes_to_read > 0:
                mess = mess + self.ser.read(bytes_to_read).decode("UTF-8")
                while ("#" in mess) and ("!" in mess):
                    start = mess.find("!")
                    end = mess.find("#")
                    self.process_data(mess[start:end + 1])
                    if end == len(mess):
                        mess = ""
                    else:
                        mess = mess[end + 1:]

    def process_data(self,data_device):
        data_device = data_device.replace("!", "")
        data_device = data_device.replace("#", "")
        split_data = data_device.split(":")
        print(split_data)
        if split_data[1] == "TEMP":
            self.adafruit_io.publish("bbc-temp", split_data[2])
def get_port():
    ports = serial.tools.list_ports.comports()
    len_port = len(ports)
    comm_port = "None"
    for i in range(0, len_port):
        port = ports[i]
        str_port = str(port)
        if "USB Serial Device" in str_port:
            split_port = str_port.split(" ")
            comm_port = (split_port[0])
    return comm_port



