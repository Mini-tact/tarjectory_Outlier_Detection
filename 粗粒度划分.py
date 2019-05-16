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
        sum += math.log(perp, 2) + math.log(angle, 2)
    return sum

def sum_all(fine, coarse):
    sum_value = 0.0
    fine_partition = []
    for c in range(len(coarse)-1):
        coarse_partition = [coarse[c], coarse[c+1]]
        """
        在确定粗端点后寻找对应的精细分区
        """
        s = fine.index(coarse_partition[0])
        e = fine.index(coarse_partition[1])

        LH_value = abs(e - s)  # 计算精细化分区的长度
        # 构建精细线段

        for i in range(LH_value):
            fine_partition.append([fine[s:e+1][i], fine[s:e+1][i+1]])

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
    for item in range(math.floor(len(data)/partition)):  # math.floor 向下取整
        coarse.append(data[item*partition])

    if len(data) % partition != 0:
        coarse.append(data[len(data)-1])

    return coarse

def mini_value(data):
    greedy_array = []
    for i in np.linspace(2, len(data)-1, len(data)-2):
        coarse = Coarse_grained_partition(data, i)  # 获取粗粒度分区
        sum_value = sum_all(data, coarse)
        greedy_array.append(sum_value)  # 将最小值放入数组排序

    index = greedy_array.index(min(greedy_array))


    return Coarse_grained_partition(data, index)  # 返回最小化L(H)+L(D|H)的值对应的粗划分集合










