import matplotlib.pyplot as plt
import pandas as pd

def graph1():
    
    data = ['Document','Picture', 'Others','Windows','Users','System_Volume_Information'] # データ名
    rate = [824,  25, 45, 23, 70, 128] # データ別の容量割合（%）
    Picture = list(range(rate[1])) + [24] * 823 # データの数をDocに合わせたPictureのデータ
    Others = list(range(rate[2])) + [44] * 823# データの数をDocに合わせたOthersのデータ
    Windows= list(range(rate[3])) + [22] * 823 # データの数をDocに合わせたWindowsのデータ
    Users   = list(range(rate[4])) + [69] * 823 # データの数をDocに合わせたUsersのデータ
    System_Volume_Information = list(range(rate[5])) + [127] * 823 # データの数をDocに合わせたSystem Value Informationデータ
    Document = range(rate[0]) # Documentのデータ

    fontsize=15
    fig, axs = plt.subplots(1, 2, figsize=(10, 5)) # 図の中に２つのサブプロット作る

    for j, u, k, i, o, p in zip(Document, Picture,Others,Windows,Users,System_Volume_Information):
        """
        棒グラフのサブプロット
        """
        axs[0].cla()
        axs[0].bar(data, [j, u, k, i, o, p], width=0.9, color=['b', '#ff7f00', 'g', 'r', '#984ea3', '#a65628'])
        axs[0].text(data[0], j+4, "{} MB".format(j), fontsize=13)
        axs[0].text(data[1], u+4, "{} MB".format(u), fontsize=13)
        axs[0].text(data[2], k+4, "{} MB".format(k), fontsize=13)
        axs[0].text(data[3], i+4, "{} MB".format(i), fontsize=13)
        axs[0].text(data[4], o+4, "{} MB".format(o), fontsize=13)
        axs[0].text(data[5], p+4, "{} MB".format(p), fontsize=13)
        axs[0].set_xlabel("Data", fontsize=fontsize)
        axs[0].set_ylabel("Rate", fontsize=fontsize)
        axs[0].set_xlim(-1, 6)
        axs[0].set_ylim(0, 1000)
        axs[0].grid()
        axs[0].set_title("Using Strage")



        """
        円グラフ用のサブプロット
        """
        axs[1].cla()
        axs[1].pie([j, u, k, i, o, p], labels=data, autopct='%1.1f%%', wedgeprops={'width': 0.6, 'linewidth': 4, 'edgecolor': 'w'})
        axs[1].set_title("Usage Rate")

        # 図のタイトル
        plt.suptitle("Using Strage", fontsize=fontsize)
        plt.pause(0.1)
        
def graph2():
    data = ['Document','Picture', 'Others','Windows','Users','System_Volume_Information'] # データ名
    rate = [62,  25, 45, 23, 50, 55] # データ別の容量割合（%）
    Picture = list(range(rate[1])) + [24] * 61 # データの数をDocに合わせたPictureのデータ
    Others = list(range(rate[2])) + [44] * 61# データの数をDocに合わせたOthersのデータ
    Windows= list(range(rate[3])) + [22] * 61 # データの数をDocに合わせたWindowsのデータ
    Users   = list(range(rate[4])) + [49] * 61 # データの数をDocに合わせたUsersのデータ
    System_Volume_Information = list(range(rate[5])) + [54] * 61 # データの数をDocに合わせたSystem Value Informationデータ
    Document = range(rate[0]) # Documentのデータ

    fontsize=15
    fig, axs = plt.subplots(1, 2, figsize=(10, 5)) # 図の中に２つのサブプロット作る

    for j, u, k, i, o, p in zip(Document, Picture,Others,Windows,Users,System_Volume_Information):
        """
        棒グラフのサブプロット
        """
        axs[0].cla()
        axs[0].bar(data, [j, u, k, i, o, p], width=0.9, color=['b', '#ff7f00', 'g', 'r', '#984ea3', '#a65628'])
        axs[0].text(data[0], j+4, "{} MB".format(j), fontsize=13)
        axs[0].text(data[1], u+4, "{} MB".format(u), fontsize=13)
        axs[0].text(data[2], k+4, "{} MB".format(k), fontsize=13)
        axs[0].text(data[3], i+4, "{} MB".format(i), fontsize=13)
        axs[0].text(data[4], o+4, "{} MB".format(o), fontsize=13)
        axs[0].text(data[5], p+4, "{} MB".format(p), fontsize=13)
        axs[0].set_xlabel("Data", fontsize=fontsize)
        axs[0].set_ylabel("Rate", fontsize=fontsize)
        axs[0].set_xlim(-1, 6)
        axs[0].set_ylim(0, 100)
        axs[0].grid()
        axs[0].set_title("Using Strage")



        """
        円グラフ用のサブプロット
        """
        axs[1].cla()
        axs[1].pie([j, u, k, i, o, p], labels=data, autopct='%1.1f%%', wedgeprops={'width': 0.6, 'linewidth': 4, 'edgecolor': 'w'})
        axs[1].set_title("Usage Rate")

        # 図のタイトル
        plt.suptitle("Using Strage", fontsize=fontsize)
        plt.pause(0.1**320)
