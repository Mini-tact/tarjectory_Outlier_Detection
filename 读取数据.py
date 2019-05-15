import scipy.io

from 粗粒度划分 import mini_value, Coarse_grained_partition

"""
FSC 2019/05/11 10:29:23
"""
def getData():
    f = open('cross.mat', 'rb')
    mdict = scipy.io.loadmat(f)
    train_data = mdict['tracks']  # TR
    # 对数据存储形式进行改变，形式为；每条轨迹，每条轨迹点的横纵坐标
    tarjectorise = []
    for tarjectory in train_data:  # 改变存储方式
        tj = []
        for x, y in zip(tarjectory[0][0], tarjectory[0][1]):
            tj.append([x, y])
        tarjectorise.append(tj)

    # 对粗粒度进行划分
    c_all = []  # 存储的是所有路径粗分区的集合和精细分区
    for item in tarjectorise:
        C = []
        C.append(Coarse_grained_partition(item, mini_value(item)))
        C.append(item)
        c_all.append(C)

    return c_all
