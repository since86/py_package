import tkinter

baseFrame = tkinter.Tk()
menubar = tkinter.Menu(baseFrame)

emenu = tkinter.Menu(menubar)

emenu1 = tkinter.Menu(menubar)

for item in ['Copy','Paste', 'Cut']:
    emenu.add_command(label=item)

for x in ['Contact','Help']:
    emenu1.add_command(label=x)

menubar.add_cascade(label='File')
menubar.add_cascade(label='Edit',menu=emenu)
menubar.add_cascade(label='About',menu=emenu1)

baseFrame['menu'] = menubar

baseFrame.mainloop()
