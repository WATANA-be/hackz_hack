def login():
    import tkinter as tk
    from tkinter import ttk
    

    # メインウィンドウ作成
    root = tk.Tk()
    root.title("security")
    root.geometry("700x500")
    ttk.Style().theme_use('clam')


    # ユーザーID
    user_label = tk.Label(text = "user")
    print()
    user_entry = tk.Entry()

    # パスワード
    pass_label = tk.Label(text = "password")
    print()
    pass_entry = tk.Entry()

    #背景の色
    root.configure(bg='gray')


    # ボタン
    button = tk.Button(text = "仕事しろ！")

    # ウィジェット配置
    user_label.pack()
    user_entry.pack()
    pass_label.pack()
    pass_entry.pack()
    button.pack()

    # 画面出力
    root.mainloop()

#login()