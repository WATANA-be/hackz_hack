#-*- coding:utf-8 -*-
import tkinter
import tkinter.ttk as ttk
##from tkinter import PhotoImage
##from PIL import Image, ImageTk
##import os
#root = tkinter.Tk()

def mail():
  # メインウィンドウを作成
  app = tkinter.Tk()
  app.title(u"Gmail")

  f = open('mail_ex.txt', 'r', encoding='UTF-8') #テキストファイル読み込み

  datalist = f.readlines() #テキストの文字列のリスト
  honbun = ""
  for i in range(len(datalist)): #リストの[]を
     bun = datalist[i]
     honbun += bun






  class Frame1(tkinter.Frame):
     def __init__(self, master):
         super().__init__(master)
        
         canvas = tkinter.Canvas(
              self,
              width=150,
              height=70,
              #bg="white"
          )
         canvas.pack()

         t1 = canvas.create_text(90, 45, text="Gmail", font=("",25))

          ##img = Image.open(os.path.dirname(__file__)+"gmail_icom.png")
          ##img = img.resize((30,30))
          ##img = ImageTk.PhotoImage(img)
          #photo = tkinter.PhotoImage(
          #      file="gmail_icom.png",master = app
          #)
          #photo = photo.resize((30,30))
          ##p1 = canvas.create_image(50,50,image = img)
        
  class Frame2(tkinter.Frame):
      def __init__(self, master):
          super().__init__(master)
              

          entry = tkinter.Entry(
              self, 
              width = 50,           
          )
          entry.pack()

        
       

  class Frame3(tkinter.Frame):
      def __init__(self,master):
          super().__init__(master)

          button = tkinter.Button(
              self,
              text="+作成",
          )
          button.pack()

          canvas = tkinter.Canvas(
              self, 
              width=150,
              height=700,
              #bg="white"
          )
          canvas.pack(fill=tkinter.BOTH)

        
        
          t1 = canvas.create_text(80, 30, text="□　受信トレイ　　　10", font=("",12))
          canvas.create_rectangle(canvas.bbox(t1))
          x0, y0, x1, y1 = canvas.bbox(t1)
          t2 = canvas.create_text(80, 50, text="☆　スター付き　　　　", font=("",12))
          t3 = canvas.create_text(80, 70, text="〇　スヌーズ中　　　　", font=("",12))
          t4 = canvas.create_text(80, 90, text="→　重要　　　　　　 　 ", font=("",12))
          t5 = canvas.create_text(80, 110, text="→　送信済み　　　　　", font=("",12))
          t6 = canvas.create_text(80, 130, text="□　下書き　　　　 　　", font=("",12))
          t7 = canvas.create_text(80, 150, text="→　カテゴリ　　　　 　 ", font=("",12))
          t8 = canvas.create_text(80, 170, text="↓　もっと見る　　 　 　", font=("",12))
        
        

       

  class Frame4(tkinter.Frame):
     def __init__(self,master):
          super().__init__(master)

          canvas = tkinter.Canvas(
              self,
              width=450,
              height=720,
              #bg="white"
          )
          canvas.pack()


          t1 = canvas.create_text(220, 25, text="←　□　〇　□　□　〇　〇　□　→　：　1/49 　＜　＞", font=("",14))
          t2 = canvas.create_text(100, 70, text="宛先　mitsubishi@gmail.com", font=("",12))
          t3 = canvas.create_text(175, 90, text="件名　【製品A】お見積送付の件（ビジネス・のまど）"
, font=("",12))
          t4 = canvas.create_text(175, 120, text="---------------------------------------------------"
, font=("",12))
          #a = 0
          #for q in range(len(honbun)):  #１文字ずつ
          #    if q%30 == 0:   #30文字目
          #      th = canvas.create_text(175+1*q,380 +1*a,text = honbun[q],font = ("",12))
          #      a = a+5
          #    else:
          #      th = canvas.create_text(175+1*q,380 +1*a,text = honbun[q],font = ("",12))
          th = canvas.create_text(220,380,text = honbun,font = ("",12))
           
          
        





  # 各部品オブジェクトを作成
  frame1 = Frame1(app)
  frame2 = Frame2(app)
  frame3 = Frame3(app)
  frame4 = Frame4(app)

  # 部品を配置
  frame1.grid(column=0,row=0)
  frame2.grid(column=1,row=0)
  frame3.grid(column=0,row=1)
  frame4.grid(column=1,row=1)

  # メインループ
  app.mainloop()
  app.close()
