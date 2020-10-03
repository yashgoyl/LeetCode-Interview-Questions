from tkinter import *
class Fahrenhit:
    def __init__(self,root):
        self.f = Frame(root, width = 600, height = 600)
        self.f.propagate(0)
        self.f.pack()
        self.l1 = Label(text = "Temp Converter F to C")
        self.e1 = Entry(self.f,width = 10)
        self.l2 = Label(text = "F")
        self.b = Button(self.f , text = "Temp in Celcius", width = 20 , height = 1, bg="cyan", activebackground = "green" , activeforeground = "black",command = self.incelcius)
        self.e2 = Entry(self.f,width = 10)
        self.l3 = Label(text = "C")

        self.l1.place(x = 50 , y = 50)
        self.e1.place(x=50 , y=80)
        self.l2.place(x = 140, y = 80)
        self.b.place(x = 50, y = 110)
        self.e2.place(x=50 , y=160)
        self.l3.place(x = 140, y = 160)
    def incelcius(self):
        f = float(self.e1.get())
        Celsius = (5/9)*(f-32)
        self.e2 = Entry(self.f,width = 10)
        self.e2.insert(0,str(Celsius))
        self.e2.place(x= 50, y = 160)

root = Tk()
root.title("B212")
a = Fahrenhit(root)
root.mainloop()