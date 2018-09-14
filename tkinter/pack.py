import tkinter

def showLabel():
    global baseFrame
    lb = tkinter.Label(baseFrame, text='显示label')
    lb.pack()

baseFrame = tkinter.Tk()

#btn = tkinter.Button(baseFrame, text='Show Label', command=showLabel, cursor=center_ptr)
#btn.pack()

for a in ['n', 's', 'e', 'w', 'ne', 'nw', 'se', 'sw']:
    tkinter.Button(baseFrame,
           text='anchor',
           anchor=a,
           command=showLabel,
           #state='disable',
           bg = 'blue',
           fg='white',
           cursor='plus',
           width=30,
           height=4).pack(expand=tkinter.YES,fill=tkinter.BOTH)


baseFrame.mainloop()