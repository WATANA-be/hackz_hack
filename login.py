from tkinter import *
from tkinter import ttk
import time
def login():# -*- coding: utf-8 -*-
    import tkinter
    import tkinter.font as f
    import math
    class PswdBox(tkinter.Tk):
        def __init__(self):
            tkinter.Tk.__init__(self)
            self.title('Enter password')
            self.label1=tkinter.Label(self,text="パスワードをここに入力")
            self.label1.pack()
            self.ent = tkinter.Entry(self, show='*')#入力内容を隠す
            self.ent.pack()
            self.lbl = tkinter.Label(self, foreground='#ff0000')
            self.lbl.pack()
            self.btn = tkinter.Button(self, text='Submit', command=self.submit)
            self.btn.pack()
            # ここで正しいパスワードを定義 あるいは ファイルからインポートなどする

            #correct_pass='passa'
            self.correct_pass = 'pass'

        def submit(self):
            self.pswd = self.ent.get()
            if self.pswd == self.correct_pass: # 正しい
                self.destroy()
                root = tkinter.Tk()
                root.title("success！")
                font1=f.Font(size=20)
                root.label2=tkinter.Label(root,text="正しいパスワードが入力されました。",font=font1)
                root.label2.pack()
                root.label3=tkinter.Label(root,text="ようこそ")
                root.label3.pack()
                root.label4=tkinter.Button(root,text='PUSH')
                root.label4.pack()
                root.label5=tkinter.Button(root,text='押す')
                root.label5.pack()

                root.geometry("700x500")
                root.configure(bg='gray')
                root.after(100000,lambda: root.destroy())
                
                root.mainloop()
                # ウィンドウを閉じる
            else: # 間違え
                self.lbl['text'] = 'パスワードが違います!'
                print(self.pswd)
                login.after(100,lambda: login.destroy())
                login.mainloop()

    if __name__ == '__main__':
        pb = PswdBox()
        pb.geometry("700x500")
        pb.after(100000,lambda: pb.destroy())
        pb.after(100000,lambda: pb.destroy())
        pb.mainloop()
        print(pb.pswd)

#login()