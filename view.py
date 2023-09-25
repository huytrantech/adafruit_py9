import tkinter as tk
from tkinter import ttk
from tkinter_component import *
import pandas as pd
import  matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from datetime import datetime
# def onClick():
#     name = txtA.get("1.0", "end")
#     age = txtB.get("1.0", "end")
# def insertTka():
#     txtA.delete(1.0, tk.END)
#     txtA.insert(tk.END , '5')

class FrameTkinter(object):
    def __init__(self, root, bg='black', position_x=0, width=500):
        self.root = root
        self.position_x = position_x
        self.width = width
        self.init_line()
        self.title_frame = ''

    def init_line(self):
        separator = tk.Frame(self.root, width=5, bg='gray')
        separator.pack(side='left', fill='y', padx=self.position_x + self.width)

    def add_title(self, title):
        self.title_frame = title
        x_title = self.width / 2
        tk.Label(text=self.title_frame).place(x=x_title, y=10, width=len(title)*10, height=40, anchor='center')


class AppTkinter(object):

    def __init__(self, title):
        self.title = title
        self.root = tk.Tk()
        self.background_color = 'white'
        self.init_app()

    def init_app(self):
        self.root.title(self.title)
        self.root.attributes('-fullscreen', True)
        self.root.configure(background=self.background_color)
        self.init_dashboard_statistics()

    def init_dashboard_statistics(self):
        font = ("Helvetica", 20)
        frame = tk.Frame(self.root,bg='white',height=70)
        frame.pack(fill='x',pady=0,padx=0)

        label = tk.Label(frame , text='Dashboard',font=font,fg='black')
        label.configure(background='white')
        label.place(x=10,y=20)

        vlist = ["Temperatur", "Humidity"]

        Combo = ttk.Combobox(self.root, values=vlist,background='white')
        Combo.set("Option1")
        Combo.configure(background='white')
        Combo.place(x=220, y=20)

        line = tk.Frame(self.root, bg='gray', height=2)
        line.pack(fill='x', pady=0, padx=0)
        self.init_value_temperature()
        self.init_chart()

    def init_value_temperature(self):
        font = ("Helvetica", 20)

        frame = tk.Frame(self.root, bg='white', height=500)
        frame.pack(fill='x', pady=0, padx=0)

        label_temp = tk.Label(frame, text='Temperature', font=font, fg='black')
        label_temp.configure(background='white')
        label_temp.place(x=40, y=20)

        line_current = tk.Frame(frame, bg='green', height=100,width=5)
        line_current.pack(side='left',pady=60, padx=40)

        label_current = tk.Label(frame, text='Current', font=font, fg='green')
        label_current.configure(background='white')
        label_current.place(x=60, y=80)

        line_min = tk.Frame(frame, bg='purple', height=100, width=5)
        line_min.pack(side='left', pady=60, padx=200)

        label_min = tk.Label(frame, text='Min', font=font, fg='purple')
        label_min.configure(background='white')
        label_min.place(x=300, y=80)

        line_max = tk.Frame(frame, bg='orange', height=100, width=5)
        line_max.pack(side='left', pady=60, padx=0)

        label_max = tk.Label(frame, text='Max', font=font, fg='orange')
        label_max.configure(background='white')
        label_max.place(x=500, y=80)

        line_avg = tk.Frame(frame, bg='red', height=100, width=5)
        line_avg.pack(side='left', pady=60, padx=200)

        label_avg = tk.Label(frame, text='Avg', font=font, fg='red')
        label_avg.configure(background='white')
        label_avg.place(x=710, y=80)

    def init_chart(self):
        data2 = {'year': [1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010],
                 'unemployment_rate': [9.8, 12, 8, 7.2, 6.9, 7, 6.5, 6.2, 5.5, 6.3],
                 'unemployment_rate_1': [22, 42, 18, 17.2, 16.9, 17, 16.5, 16.2, 15.5, 16.3]
                 }
        df_base = pd.DataFrame(data2)

        figure2 = plt.Figure(figsize=(5, 4), dpi=100)
        ax2 = figure2.add_subplot(111)
        line2 = FigureCanvasTkAgg(figure2, self.root)
        line2.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
        df2 = df_base[['year', 'unemployment_rate']].groupby('year').sum()
        df2.plot(kind='line', legend=True, ax=ax2, color='r', marker='o', fontsize=10)
        ax2.set_title('Year Vs. Unemployment Rate')

        figure3 = plt.Figure(figsize=(5, 4), dpi=100)
        ax3 = figure3.add_subplot(111)
        line3 = FigureCanvasTkAgg(figure3, self.root)
        line3.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
        df3 = df_base[['year', 'unemployment_rate_1']].groupby('year').sum()
        df3.plot(kind='line', legend=True, ax=ax3, color='r', marker='o', fontsize=10)
        ax2.set_title('Year Vs. Unemployment Rate 1')
        pass

    def run_app_mainloop(self):
        self.root.mainloop()


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

app = AppTkinter('IoT Application')

menu = TopMenuApp([
    MenuDto('dashboard',
            menu_child=[
                MenuDto('sensors',[]),
                MenuDto('controllers',[])]),
    MenuDto('file',menu_child=[MenuDto('export csv',[])])])
menu.init(app.root)

app.run_app_mainloop()
# export DISPLAY=:0.0 when run on resbery pi when show error no display
