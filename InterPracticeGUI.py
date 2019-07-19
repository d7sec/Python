# import tkinter standard Python Library to create GUIs
# Just a practice run for CW
from tkinter import Tk, Label, Button

# creating the GUI Class, which holds the ROOT (main window) 
# 2 Buttons, Greet / Close and a Label)
class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("Python GUI Practice")

        self.label = Label(master, text="This is our first GUI!")
        self.label.pack()

        self.greet_button = Button(master, text="Greet", command=self.greet)
        self.greet_button.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()
    
    def greet(self):
        print("Greetings!")

root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()