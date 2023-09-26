import random
import datetime


class Task3:
    def __init__(self, tkinter_app=None):
        self._tkinter_app = tkinter_app
        print("Init task 3")
        return

    def Task3_Run(self):
        time_value = datetime.datetime.now().strftime("%H:%M:%S")
        rand_value = random.randint(0, 100)
        try:
            self._tkinter_app.add_new_value_chart({'time': time_value, 'value': rand_value})
            self._tkinter_app.init_chart()
        except:
            print('app is not working')
        print("Task 3 is activated!!!!")
