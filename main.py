import time
from tkinter import *

mode = False
reseted = True
start_time = time.time()
interval = 0

def start_stop():
    global mode
    global reseted
    mode = not mode
    if mode:
        reseted = False

def reset():
    global mode
    global start_time
    global reseted
    mode = False
    reseted = True
    start_time = time.time()
    minLabel.configure(text = '0')
    secLabel.configure(text = '00')

def task():
    global start_time
    global interval
    if mode:
        interval = time.time() - start_time
        min = int(interval/60)
        sec = round(interval % 60, 2)
        minLabel.configure(text=min)
        secLabel.configure(text=sec)
    else:
        if not reseted:
            start_time = time.time() - interval
        else:
            start_time = time.time()
    app.after(10, task)

app = Tk()
app.configure(width=500, height=200, bg='blue')
app.wm_resizable(width=False, height=False)
app.title('Stop Watch')
minLabel = Label(app, text='0', font=('ariel', 50), bg='blue', fg='white')
Label(app, text=':', font=('ariel', 50), bg='blue', fg='white').place(x=200, y=20)
secLabel = Label(app, text='00', font=('ariel', 50), bg='blue', fg='white')
minLabel.place(x = 100, y = 20)
secLabel.place(x = 300, y = 20)
startBtn = Button(app, text=' Start/Stop ', font=('ariel', 20), bg='green', command = start_stop)
RstBtn = Button(app, text=' Reset ', font=('ariel', 20), bg='green', command = reset)
startBtn.place(x = 100, y = 130)
RstBtn.place(x = 270, y = 130)
app.after(10, task)
app.mainloop()