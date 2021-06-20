import tkinter as tk

# メインウィンドウ作成
root = tk.Tk()
root.title("ログイン画面")
root.geometry("800x600")

# ユーザーID
user_label = tk.Label(text = "user")
user_entry = tk.Entry()

# パスワード
pass_label = tk.Label(text = "password")
pass_entry = tk.Entry()


if user_label==user_entry and pass_label==pass_entry:
    root.after(1,lambda: root.destroy())
    root2 = tk.Tk()
    root2.title("ログイン画面")
    root2.geometry("800x600")
    

# ボタン
button = tk.Button(text = "login")

# ウィジェット配置
user_label.pack()
user_entry.pack()
pass_label.pack()
pass_entry.pack()
button.pack()

# 画面出力
root.mainloop()