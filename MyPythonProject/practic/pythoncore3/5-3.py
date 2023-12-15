import tkinter

def resize(ev=None):
    label.config(font='helvetica -%d bold'%scale.get())

top=tkinter.Tk()
label=tkinter.Label(top,text='hello world!',font='helvetica -12 bold')
label.pack()
scale=tkinter.Scale(top,from_=10,to=40,orient='horizontal',command=resize)
scale.pack()
tkinter.mainloop()
