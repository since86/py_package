import tkinter

base = tkinter.Tk()

base.wm_title('test')

lb = tkinter.Label(base, text='Python Label')
lb.pack()

lb1 = tkinter.Label(base, text= '蓝色', background='blue')
lb1.pack()

lb2 = tkinter.Label(base, text= '绿色', background='green')
lb2.pack()

base.mainloop()