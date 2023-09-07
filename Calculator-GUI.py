from tkinter import *


class My_Calc:
    def __init__(self, Calc):
        self.lbl1 = Label(Calc, text='FIRST NUMBER')
        self.lbl2 = Label(Calc, text='SECOND NUMBER')
        self.lbl3 = Label(Calc, text='RESULT')
        self.t1 = Entry(bd=3)
        self.t2 = Entry(bd=3)
        self.t3 = Entry(bd=3)
        self.btn1 = Button(Calc, text='ADD')
        self.btn1 = Button(Calc, text='SUBTRACT')
        self.lbl1.place(x=100, y=50)
        self.t1.place(x=200, y=50)
        self.lbl2.place(x=100, y=100)
        self.t2.place(x=200, y=100)
        self.b1 = Button(Calc, text='ADD', command=self.add)
        self.b2 = Button(Calc, text='SUBTRACT')
        self.b2.bind('<BUTTON-1>', self.sub)
        self.b1.place(x=100, y=150)
        self.b2.place(x=200, y=150)
        self.lbl3.place(x=100, y=150)
        self.t3.place(x=200, y=200)
    def add(self):
        self.t3.delete(0, 'end')
        num1 = int(self.t1.get())
        num2 = int(self.t2.get())
        result = num1+num2
        self.t3.insert(END, str(result))
    def sub(self, event):
        self.t3.delete(0, 'end')
        num1 = int(self.t1.get())
        num2 = int(self.t2.get())
        result = num1 - num2
        self.t3.insert(END, str(result))

Cal=Tk()
myCalc = My_Calc(Cal)
Cal.title("HELLO NEW CAlC")
Cal.geometry("500x250+10+10")
Cal.mainloop()
