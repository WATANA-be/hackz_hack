def todo():
    # -*- coding:utf-8 -*-
    import tkinter
    from tkinter import font
    
    # 遅らせて実行される関数
    def func():
        

        # ラベルのテキストを変更
        label.config(
            text="□電話",
            bg='gray'
        )
        #label.place(x=-50,y=0)
    def func2():
        

        label.config(
            text="□電話\n□slack",
            bg='gray'
        )
    def func3():
        

        label.config(
            text="〼電話\n□slack\n□趣味開発\n□bot製作 \n",
            bg='gray'
        )

    def func4():
        

        label.config(
            text="〼電話\n□slack\n〼趣味開発\n□bot製作 \n",
            bg='gray'
        )

    def func41():
        

        label.config(
            text="〼電話\n〼slack\n〼趣味開発\n□bot製作 \n",
            bg='gray'
        )

    def func5():
        

        label.config(
            text="〼電話\n□slack\n〼趣味開発\n〼bot製作\n□ハッカソン\n□筋トレ\n□課題",
            bg='gray'
        )

    def func51():
        

        label.config(
            text="〼電話\n□slack\n〼趣味開発\n〼bot製作\n□ハッカソン\n〼筋トレ\n□課題",
            bg='gray'
        )

    def func52():
        

        label.config(
            text="〼電話\n□slack\n〼趣味開発\n〼bot製作\n□ハッカソン\n〼筋トレ\n〼課題",
            bg='gray'
        )

    def func6():
        

        label.config(
            text="〼電話\n□slack\n〼趣味開発\n〼bot製作\n〼ハッカソン\n□筋トレ\n〼課題",
            bg='gray'
        )

    def func7():
        

        label.config(
            text="〼電話\n〼slack\n〼趣味開発\n〼bot製作\n〼ハッカソン\n□筋トレ\n〼課題\n□バグ直し\n□趣味開発(再)\n□atcoder",
            bg='gray'
        )

    def func8():
        

        label.config(
            text="〼電話\n〼slack\n〼趣味開発\n〼bot製作\n〼ハッカソン\n〼筋トレ\n〼課題\n□バグ直し\n〼趣味開発(再)\n□atcoder",
            bg='gray'
        )

    def func81():
    

        label.config(
            text="〼電話\n〼slack\n〼趣味開発\n〼bot製作\n〼ハッカソン\n〼筋トレ\n〼課題\n□バグ直し\n〼趣味開発(再)\n〼atcoder",
            bg='gray'
        )

    def func9():
    

        label.config(
            text="〼電話\n〼slack\n〼趣味開発\n〼bot製作\n〼ハッカソン\n〼筋トレ\n〼課題\n〼バグ直し\n〼趣味開発(再)\n〼atcoder",
            bg='gray'
        )

    

    def func10():
    

        label.config(
            text="                  DONE!!!!!!!",
            bg='lightgray'
        )

    # メインウィンドウの作成
    app = tkinter.Tk()
    app.geometry("500x400")

    #fontの指定
    font1 = font.Font(size=30)

    # ラベルウィジェット作成
    label = tkinter.Label(
        app,
        width=50,
        height=20,#ここが、数字が表示される場所だべ、ここの範囲を小さくしすぎて文字が切れてた
        font = font1,
        anchor="w"

    )
    label.pack()
    


    # 3000ms後にfunc関数を実行
    app.after(1000, func)
    app.after(4000,func2)
    app.after(6000,func3)
    app.after(7000,func4)
    app.after(9500,func41)
    app.after(10000,func5)
    app.after(12500,func51)
    app.after(13800,func52)
    app.after(15000,func6)
    app.after(16000,func7)
    app.after(17000,func8)
    app.after(18000,func8)
    app.after(18500,func8)
    app.after(19000,func9)
    app.after(21000,func10)
    # メインループ
    app.title("TODO")
    app.mainloop()
#todo()#これはつばきち側の処理で！