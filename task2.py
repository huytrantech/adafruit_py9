import random


class Task2:
    def __init__(self, tkinter_app=None):
        self._tkinter_app = tkinter_app
        print("Init task 2")
        return

    def Task2_Run(self):
        v_min = random.randint(0, 100)
        v_max = random.randint(0, 100)
        v_avg = random.randint(0, 100)
        v_current = random.randint(0, 100)

        self._tkinter_app.set_label_value(min_arg=v_min, max_arg=v_max, avg_arg=v_avg, current_arg=v_current)
        print("Task 2 is activated!!!!")
