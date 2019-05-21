#coding:utf-8
import math
from define import distance_between_T_Partitions
import numpy as np

def LDH(fine, coarse):
    """
    图7中的公式,计算的为一个粗线段和多个精准线段的垂直距离和角距的和
    :param fine:
    :param coarse:
    :return:
    """
    sum = 0.0  # L(D|H)的值
    for i in range(len(fine)):
        perp = abs(distance_between_T_Partitions(coarse[0], coarse[1], fine[i][0], fine[i][1]).perpendicular())
        angle = distance_between_T_Partitions(coarse[0], coarse[1], fine[i][0], fine[i][1]).angle_distance()
        if perp == 0:
            print('the perp is zero')
            sum += math.log(angle, 2)
        else:
            if angle == 0:
                print('the angle is zero')
                sum += math.log(perp, 2)
            else:
                sum += math.log(perp, 2) + math.log(angle, 2)
    return sum

def deal_error(fine, coarse_partition, total, s, e):
    """
    细粒度划分的搜影
    :param fine:
    :param coarse_partition:
    :param total:
    :param s:
    :param e:
    :return:
    """
    item_i = [i for i, item in enumerate(fine) if item == coarse_partition[0]]
    item_j = [j for j, item in enumerate(fine) if item == coarse_partition[1]]

    for e_e in item_j:
        for s_s in item_i:
            if e_e - s == int(total):
                e = e_e
                return s, e

            elif e_e - s_s == int(total):
                s = s_s
                e = e_e
                return s, e
            else:
                print('粗粒度索引划分失败')
                print(e, s, total)
                print(item_i)
                print('----------------------------------')
                print(item_j)
                print('------------end----------------')

def sum_all(fine, coarse, total):
    sum_value = 0.0
    for c in range(len(coarse)-1):
        if coarse[c] == coarse[c+1]:  # 去除连续点重合
            continue
        coarse_partition = [coarse[c], coarse[c+1]]

        """
        在确定粗端点后寻找对应的精粒度索引
        """
        s = fine.index(coarse_partition[0])
        e = fine.index(coarse_partition[1])

        LH_value = e - s  # 计算精细化分区的长度s
        # 构建精细线段
        """
        处理错误的粗粒度索引
        """
        if LH_value <= 0:
            s, e = deal_error(fine, coarse_partition, total, s, e)
            LH_value = e - s

        """
        获取粗粒度对应的细粒度
        """
        fine_partition = []  # 重置数组
        for i in range(LH_value):
            if fine[s:e+1][i] == fine[s:e+1][i+1]:# 去除连续点重合和零点
                pass
            else:
                fine_partition.append([fine[s:e+1][i], fine[s:e+1][i+1]])

        # print(coarse_partition)
        # print('-----------end-------------')
        LDH_value = LDH(fine_partition, coarse_partition)
        sum_value = sum_value + LH_value + LDH_value
    return sum_value

def Coarse_grained_partition(data, partition):
    """
    按照一定规则对线进行粗粒度划分
    :param data:
    :param partition:粗粒度划分标准对于等于1
    :return:
    """
    partition = int(partition)
    # 对线进行划分：等距离取点
    coarse = []
    for item in range(int(math.floor(len(data)/partition))):  # math.floor 向下取整
        coarse.append(data[item*partition])

    return coarse

def mini_value(data):
    greedy_array = []
    for i_iter in range(2, math.floor(len(data)/2)):
        coarse = Coarse_grained_partition(data, i_iter)  # 获取粗粒度分区
        sum_value = sum_all(data, coarse, i_iter)
        greedy_array.append(sum_value)

    index = greedy_array.index(min(greedy_array))  # 将最小值放入数组排序
    return Coarse_grained_partition(data, index+2)  # 返回最小化L(H)+L(D|H)的值对应的粗划分集合










