import tkinter as tk


def onClick():
    name = txtA.get("1.0", "end")
    age = txtB.get("1.0", "end")
def insertTka():
    txtA.delete(1.0, tk.END)
    txtA.insert(tk.END , '5')

window = tk.Tk()
window.title("Python app")
# window.geometry("600x400")
window.attributes('-fullscreen', True)

labelA = tk.Label(text="Student name")
labelA.place(x=5, y=5, width=80, height=30)

txtA = tk.Text()
txtA.place(x=85, y=5, width=100, height=30)

labelB = tk.Label(text="Student Age")
labelB.place(x=5, y=35, width=80, height=30)

txtB = tk.Text()
txtB.place(x=85, y=35, width=100, height=30)

button = tk.Button(text="save", command=onClick)
button.place(x=5, y=125, width=100, height=50)

# export DISPLAY=:0.0 when run on resbery pi when show error no display