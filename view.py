import time
import tkinter as tk
from tkinter import ttk
from tkinter_component import *
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


# def onClick():
#     name = txtA.get("1.0", "end")
#     age = txtB.get("1.0", "end")
# def insertTka():
#     txtA.delete(1.0, tk.END)
#     txtA.insert(tk.END , '5')


class AppTkinter(object):

    def __init__(self, title):
        self.title = title
        self._root = tk.Tk()
        self.background_color = 'white'
        self.sensors = ["Temperature", "Humidity"]
        self._label_sensors = self.sensors[0]
        self._label_current = None
        self._label_min = None
        self._label_max = None
        self._label_avg = None
        self._data_chart = {
            'time': [],
            'value': []
        }
        self.fig = plt.Figure(figsize=(15, 10), dpi=100)
        self.plot = self.fig.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.fig, master=self._root)
        self.init_app()

    def _init_menu(self):
        menu = TopMenuApp([
            MenuDto('dashboard',
                    menu_child=[
                        MenuDto('sensors', []),
                        MenuDto('controllers', [])]),
            MenuDto('file', menu_child=[MenuDto('export csv', [])])])
        menu.init(self._root)

    def init_app(self):
        self._init_menu()
        self._root.title(self.title)
        self._root.attributes('-fullscreen', True)
        self._root.configure(background=self.background_color)
        self.init_dashboard_statistics()
        self.init_dashboard_sensor()
        self.init_chart()

    def init_dashboard_statistics(self):
        font = ("Helvetica", 20)
        frame = tk.Frame(self._root, bg='white', height=70)
        frame.pack(fill='x', pady=0, padx=0)

        label = tk.Label(frame, text='Dashboard', font=font, fg='black')
        label.configure(background='white')
        label.place(x=10, y=20)

        sensor_list = self.sensors

        Combo = ttk.Combobox(self._root, values=sensor_list, background='white', state='readonly')
        Combo.set(self.sensors[0])
        Combo.configure(background='white')
        Combo.place(x=220, y=20)

        line = tk.Frame(self._root, bg='gray', height=2)
        line.pack(fill='x', pady=0, padx=0)

    def init_dashboard_sensor(self):
        font = ("Helvetica", 20)

        frame = tk.Frame(self._root, bg='white', height=500)
        frame.pack(fill='x', pady=0, padx=0)

        label_sensors = tk.Label(frame, text=self._label_sensors, font=font, fg='black')
        label_sensors.configure(background='white')
        label_sensors.place(x=40, y=20)

        line_current = tk.Frame(frame, bg='green', height=100, width=5)
        line_current.pack(side='left', pady=60, padx=40)

        self._label_current = tk.Label(frame, text='Current', font=font, fg='green')
        self._label_current.configure(background='white')
        self._label_current.place(x=60, y=80)

        line_min = tk.Frame(frame, bg='purple', height=100, width=5)
        line_min.pack(side='left', pady=60, padx=200)

        self._label_min = tk.Label(frame, text='Min', font=font, fg='purple')
        self._label_min.configure(background='white')
        self._label_min.place(x=300, y=80)

        line_max = tk.Frame(frame, bg='orange', height=100, width=5)
        line_max.pack(side='left', pady=60, padx=0)

        self._label_max = tk.Label(frame, text='Max', font=font, fg='orange')
        self._label_max.configure(background='white')
        self._label_max.place(x=500, y=80)

        line_avg = tk.Frame(frame, bg='red', height=100, width=5)
        line_avg.pack(side='left', pady=60, padx=200)

        self._label_avg = tk.Label(frame, text='Avg', font=font, fg='red')
        self._label_avg.configure(background='white')
        self._label_avg.place(x=710, y=80)

    def set_data_chart(self, data_chart):
        self._data_chart = data_chart

    def init_chart(self):

        if len(self._data_chart['time']) < 10:
            x = self._data_chart['time']
            y = self._data_chart['value']
        else:
            x = self._data_chart['time'][-10:]
            y = self._data_chart['value'][-10:]
        print(x)

        # Vẽ biểu đồ
        self.plot.clear()
        self.plot.plot(x, y, label="Dữ liệu mẫu")
        self.plot.set_xlabel("Time")
        self.plot.set_ylabel("Value")
        self.plot.set_title("Biểu đồ mẫu")
        self.plot.legend()

        # Tạo canvas để hiển thị biểu đồ trên giao diện Tkinter
        # canvas = FigureCanvasTkAgg(self.fig, master=self._root)
        canvas_widget = self.canvas.get_tk_widget()
        canvas_widget.pack()
        self.canvas.draw()
        # self.canvas.draw()

        pass

    def run_app_mainloop(self):
        self._root.mainloop()

    def run_app_update(self):
        self._root.update()

    def set_label_value(self, min_arg=None, max_arg=None, current_arg=None, avg_arg=None):
        if min_arg is not None:
            self._label_min.config(text=min_arg)

        if max_arg is not None:
            self._label_max.config(text=max_arg)

        if avg_arg is not None:
            self._label_avg.config(text=avg_arg)

        if current_arg is not None:
            self._label_current.config(text=current_arg)

    def add_new_value_chart(self, value):
        self._data_chart['time'].append(value['time'])
        self._data_chart['value'].append(value['value'])

# window = tk.Tk()
# window.title("Python app")
# # window.geometry("600x400")
# window.attributes('-fullscreen', True)
#

# labelA = tk.Label(text="Student name")
# labelA.place(x=5, y=5, width=80, height=30)
#
# txtA = tk.Text()
# txtA.place(x=85, y=5, width=100, height=30)
#
# labelB = tk.Label(text="Student Age")
# labelB.place(x=5, y=35, width=80, height=30)
#
# txtB = tk.Text()
# txtB.place(x=85, y=35, width=100, height=30)
#
# button = tk.Button(text="save", command=onClick)
# button.place(x=5, y=125, width=100, height=50)

# app = AppTkinter('IoT Application')
# app.set_label_value(min_arg=10)
#
# app.run_app_mainloop()
# export DISPLAY=:0.0 when run on resbery pi when show error no display
