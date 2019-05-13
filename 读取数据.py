import scipy.io

from 粗粒度划分 import mini_value, Coarse_grained_partition

"""
FSC 2019/05/11 10:29:23
"""
def getData():
    f = open('cross.mat', 'rb')
    mdict = scipy.io.loadmat(f)
    train_data = mdict['tracks']  # TR
    train_label = mdict['truth']
    a = train_label.flatten()  # 矩阵
    # 对粗粒度进行划分

    c_all =[]# 存储的是所有路径粗分区的集合和精细分区
    for item in train_data:
        C = []
        C.append(Coarse_grained_partition(item,mini_value(item)))
        C.append(item)
        c_all.append(C)

    return c_all




    # x = []  # 保存训练数据
    # y = []  # 保存标签
    # for i in range(len(train_label)):
    #     if a[i] == 1 or a[i] == 8 or a[i] == 9 or a[i] == 5:
    #         x.append(train_data[i])
    #         y.append(a[i])
    # for i in range(len(y)):
    #     if y[i] == 1:
    #         y[i] = -1
    #     else:
    #         y[i] = 1
    #
    # data = []
    # for i in range(len(x)):
    #     point = []
    #     for j in range(len(x[i][0][0])):
    #         point.append([x[i][0][0][j], x[i][0][1][j]])
    #     data.append(point)
    #
    # return data  # 保存数据

