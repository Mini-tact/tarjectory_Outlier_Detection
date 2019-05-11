import scipy.io
"""
FSC 2019/05/11 10:29:23
"""
def getData():
    f = open('cross.mat', 'rb')
    mdict = scipy.io.loadmat(f)
    train_data = mdict['tracks']  # TR
    train_label = mdict['truth']
    a = train_label.flatten()  # 矩阵

    """
    在粗粒度上分区TR
    """

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

