from Tkinter import *
import tkMessageBox

class Application(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.nameInput = Entry(self)
        self.nameInput.pack()
        self.alertButton = Button(self,text="hello",command=self.hello)
        self.alertButton.pack()

    def hello(self):
        name = self.nameInput.get() or "world"
        tkMessageBox.showinfo('message','hello,%s' % name)



app = Application()
app.master.title("tello hantao")
app.mainloop()