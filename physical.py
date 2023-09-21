import time
import serial.tools.list_ports

print("RS485")
print("Sensors and Actuators")

try:
    # ls /dev/tty* lenh tim cong com
    ser = serial.Serial(port="/dev/tty.usbserial-A50285BI", baudrate=9600)
except:
    print("Can not open the port")


class PhysicalTask(object):

    def __init__(self):
        self.relay1_ON = [0, 6, 0, 0, 0, 255, 200, 91]
        self.relay1_OFF = [0, 6, 0, 0, 0, 0, 136, 27]
        self.relay2_ON = [15, 6, 0, 0, 0, 255, 200, 164]
        self.relay2_OFF = [15, 6, 0, 0, 0, 0, 136, 228]
        try:
            # ls /dev/tty* lenh tim cong com
            ser = serial.Serial(port="/dev/tty.usbserial-A50285BI", baudrate=9600)
        except:
            print("Can not open the port")
        self.ser = ser
        self.soil_moisture =  [1, 3, 0, 7, 0, 1, 53, 203]
        self.soil_temperature = [1, 3, 0, 6, 0, 1, 100, 11]

    def set_device1(self, state):
        if state:
            ser.write(self.relay1_ON)
        else:
            ser.write(self.relay1_OFF)
        time.sleep(1)
        print(self.serial_read_data())

    def set_device2(self, state):
        if state:
            ser.write(self.relay2_ON)
        else:
            ser.write(self.relay2_OFF)

    def serial_read_data(self):
        bytesToRead = self.ser.inWaiting()
        if bytesToRead > 0:
            out = self.ser.read(bytesToRead)
            data_array = [b for b in out]
            print(data_array)
            if len(data_array) >= 7:
                array_size = len(data_array)
                value = data_array[array_size - 4] * 256 + data_array[array_size - 3]
                return value
            else:
                return -1
        return 0

    def readMoisure(self):
        self.serial_read_data()
        self.ser.write(self.soil_moisture)
        time.sleep(1)
        return self.serial_read_data()

    def readTemperature(self):
        self.serial_read_data()
        self.ser.write(self.soil_temperature)
        time.sleep(1)
        return self.serial_read_data()


