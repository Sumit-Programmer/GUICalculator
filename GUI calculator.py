from tkinter import Tk, Entry, Button, StringVar

class Calculator():
    def __init__(self, master):
        master.title("WirelessCoder")
        master.geometry("357x420+0+0")
        master.config(bg="#000000")
        master.resizable(False, False)

        self.equation = StringVar()
        self.enter_value = ''
        Entry(width=17, bg='#6C6C6C', font=('Arial', 28),foreground="#FFFB25", textvariable=self.equation).place(x=0, y=0)
        Button(width=11, height=4, text="(", relief="flat", bg="#252525", fg='#ffffff', command=lambda: self.show("(")).place(x=0,y=50)
        Button(width=11, height=4, text=")", relief="flat", bg="#252525", fg='#ffffff', command=lambda: self.show(")")).place(x=90,y=50)
        Button(width=11, height=4, text="%", relief="flat", bg="#252525", fg='#ffffff', command=lambda: self.show("%")).place(x=180,y=50)
        Button(width=11, height=4, text="1", relief="flat", bg="#252525", fg='#ffffff', command=lambda: self.show("1")).place(x=0,y=125)
        Button(width=11, height=4, text="2", relief="flat", bg="#252525", fg='#ffffff', command=lambda: self.show("2")).place(x=90,y=125)
        Button(width=11, height=4, text="3", relief="flat", bg="#252525", fg='#ffffff', command=lambda: self.show("3")).place(x=180,y=125)
        Button(width=11, height=4, text="4", relief="flat", bg="#252525", fg='#ffffff', command=lambda: self.show("4")).place(x=0,y=200)
        Button(width=11, height=4, text="5", relief="flat", bg="#252525", fg='#ffffff', command=lambda: self.show("5")).place(x=90,y=200)
        Button(width=11, height=4, text="6", relief="flat", bg="#252525", fg='#ffffff', command=lambda: self.show("6")).place(x=180,y=200)
        Button(width=11, height=4, text="7", relief="flat", bg="#252525", fg='#ffffff', command=lambda: self.show("7")).place(x=0,y=275)
        Button(width=11, height=4, text="8", relief="flat", bg="#252525", fg='#ffffff', command=lambda: self.show("8")).place(x=180,y=275)
        Button(width=11, height=4, text="9", relief="flat", bg="#252525", fg='#ffffff', command=lambda: self.show("9")).place(x=90,y=275)
        Button(width=11, height=4, text="0", relief="flat", bg="#252525", fg='#ffffff', command=lambda: self.show("0")).place(x=90,y=350)
        Button(width=11, height=4, text=".", relief="flat", bg="#252525", fg='#ffffff', command=lambda: self.show(".")).place(x=180,y=350)
        Button(width=11, height=4, text="+", relief="flat", bg="#252525", fg='#ffffff', command=lambda: self.show("+")).place(x=270,y=275)
        Button(width=11, height=4, text="-", relief="flat", bg="#252525", fg='#ffffff', command=lambda: self.show("-")).place(x=270,y=200)
        Button(width=11, height=4, text="/", relief="flat", bg="#252525", fg='#ffffff', command=lambda: self.show("/")).place(x=270,y=50)
        Button(width=11, height=4, text="x", relief="flat", bg="#252525", fg='#ffffff', command=lambda: self.show("*")).place(x=270,y=125)
        Button(width=11, height=4, text="=", relief="flat", bg="#1EFF83", fg='red', command=self.solve).place(x=270, y=350)
        Button(width=11, height=4, text="C", relief="flat", command=self.clear).place(x=0, y=350)

    def show(self, value):
        self.enter_value+=str(value)
        self.equation.set(self.enter_value)

    def clear(self):
        self.enter_value=""
        self.equation.set(self.enter_value)

    def solve(self):
        result = eval(self.enter_value)
        self.equation.set(result)

root = Tk()
calculator = Calculator(root)
root.mainloop()