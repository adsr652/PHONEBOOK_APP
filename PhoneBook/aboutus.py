from tkinter import *
from tkinter import *




class About(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)

        self.geometry("550x550+550+200")
        self.title("About US")
        self.resizable(False,False)

        self.top = Frame(self, height=550, width=550, bg='#ffa550')
        self.top.pack(fill=BOTH)


        self.text = Label(self.top, text='Hey this is About Us Page'
                                         '\n this application is made of educational purpose'
                                         '\n you can contact us Instagram, facebook, linkedin', font='arial 14 bold', bg='#ffa500',fg="white")

        self.text.place(x=50, y=50)