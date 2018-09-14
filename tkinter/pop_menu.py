import tkinter

def makeLabel():
    global baseFrame
    tkinter.Label(baseFrame, text='弹出菜单').pack()

baseFrame = tkinter.Tk()
menubar = tkinter.Menu(baseFrame)

for item in ['aa','bb','cc']:
    menubar.add_command(label=item)
    menubar.add_separator()

menubar.add_command(label='dd',command=makeLabel)

def pop(event):
    menubar.post(event.x_root,event.y_root)

baseFrame.bind('<Button-3>', pop)

baseFrame.mainloop()

