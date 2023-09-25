import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from calendar import month_name
from datetime import datetime

root = tk.Tk()

# config the root window
root.geometry('300x200')
root.resizable(False, False)
root.title('Combobox Widget')


# create a combobox
selected_month = tk.StringVar()
month_cb = ttk.Combobox(root, textvariable=selected_month)

# get first 3 letters of every month name

month_cb['values'] = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

# prevent typing a value
month_cb['state'] = 'readonly'

# place the widget
month_cb.pack(fill=tk.X, padx=5, pady=5)


# bind the selected value changes
# def month_changed(event):
#     """ handle the month changed event """
#     showinfo(
#         title='Result',
#         message=f'You selected {selected_month.get()}!'
#     )
#
#
# month_cb.bind('<<ComboboxSelected>>', month_changed)

# set the current month
current_month = datetime.now().strftime('%b')
month_cb.set(current_month)
print(current_month)

root.mainloop()