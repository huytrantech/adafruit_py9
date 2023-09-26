import datetime
class TaskMQTT:
    def __init__(self, tkinter_app=None):
        print("Init task mqtt")
        self._humidity_value = 0
        self._temperature_value = 0
        self._tkinter_app = tkinter_app
        self._ai = 'None'
        return

    def TaskMQTT_Run(self):
        try:
            time_value = datetime.datetime.now().strftime("%H:%M:%S")
            self._tkinter_app.set_label_value(current_arg=self._temperature_value,min_arg=self._ai)
            self._tkinter_app.add_new_value_chart({'time': time_value, 'value': self._temperature_value})
            self._tkinter_app.init_chart()
        except:
            print('app is not working')
        print("Task 2 is activated!!!!")

    def set_value(self, humidity_arg=None, temperature_arg=None,ai_arg=None):
        print('set value')
        if humidity_arg is not None:
            self._humidity_value = humidity_arg
        if temperature_arg is not None:
            self._temperature_value = temperature_arg

        if ai_arg is not None:
            self._ai = ai_arg
