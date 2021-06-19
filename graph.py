import matplotlib.pyplot as plt
import pandas as pd

data = ['Document', 'Others','Windows','Picture','Users','System Value Information'] # データ名
wariai = [45, 13, 6, 11, 11, 6] # データ別の容量割合（%）
Others = list(range(wariai[1])) + [12] * 44 # データの数をDocに合わせたOthersのデータ
Windows = list(range(wariai[2])) + [5] * 44# データの数をDocに合わせたWindowsのデータ
Picture = list(range(wariai[3])) + [10] * 44 # データの数をDocに合わせたPictureのデータ
Users = list(range(wariai[4])) + [10] * 44 # データの数をDocに合わせたUsersのデータ
System_Value_Information = list(range(wariai[5])) + [5] * 44 # データの数をDocに合わせたSystem Value Informationデータ
Document = range(wariai[0]) # Documentのデータ

fontsize=15
fig, axs = plt.subplots(1, 2, figsize=(10, 5)) # 図の中に２つのサブプロット作る

for j, u, k, i, o, p in zip(Document, Others,Windows,Picture,Users,System_Value_Information):

    """
    円グラフ用のサブプロット
    """
    axs[0].cla()
    axs[0].pie([j, u, k, i, o, p], labels=data, autopct='%1.1f%%', wedgeprops={'width': 0.6, 'linewidth': 4, 'edgecolor': 'w'})
    axs[0].set_title("graph circle")

    # 図のタイトル
    plt.suptitle("Population comparison between Japan and the United States", fontsize=fontsize)
    plt.pause(0.1)
