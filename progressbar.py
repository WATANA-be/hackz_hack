
from tkinter import *
from tkinter import ttk

def button_click():
    pbval.set(pbval.get() + 1)
    if pbval.get() > 10:
        pbval.set(0)

if __name__ == '__main__':
    root = Tk()
    ttk.Style().theme_use('aqua')
    root.title('Progress')
    root.columnconfigure(0, weight=1);
    root.rowconfigure(0, weight=1);

    # Frame
    frame1 = ttk.Frame(root, padding=10)
    frame1.grid(sticky=(N, W, S, E))
    frame1.columnconfigure(0, weight=1);
    frame1.rowconfigure(0, weight=1);

    # プログレスバー (確定的)
    pbval = IntVar(value=3)
    pb = ttk.Progressbar(
        frame1,
        orient=HORIZONTAL,
        variable=pbval,
        maximum=10,
        length=200,
        mode='determinate')
    pb.grid(row=0, column=0, sticky=(N, E, S, W))

    

    # 進捗ボタン
    button1 = ttk.Button(
        frame1, text='NEXT', width=5,
        command=button_click)
    button1.grid(row=0, column=1, padx=5, sticky=(E))

    # プログレスバー (不確定的)
    pb2 = ttk.Progressbar(
        frame1,
        orient=HORIZONTAL,
        maximum=10,
        value=0,
        length=200,
        mode='indeterminate')
    pb2.grid(row=1, column=0, sticky=(N, E, S, W))
    pb2.start(100)


    

    root.mainloop()