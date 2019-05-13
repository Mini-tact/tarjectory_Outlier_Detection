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
    for i in range(len(fine))-1:
        perp = distance_between_T_Partitions(coarse[0], coarse[1], fine[i], fine[i+1]).perpendicular()
        angle = distance_between_T_Partitions(coarse[0], coarse[1], fine[i], fine[i+1]).angle_distance()
        return math.log(perp, 2)+math.log(angle, 2)

def sum_all(fine, coarse):
    sum_value = 0.0
    fine_partition = []
    for c in len(coarse)-1:
        coarse_partition = [coarse[c], coarse[c+1]]
        """
        在确定粗端点后寻找对应的精细分区
        """
        for i, f in enumerate(fine):
            if f == coarse_partition[0]:  # 寻找粗线段对应的精细分区的开始端点
                flag = i  # 记录开始端点进行
            else:
                if f == coarse_partition[1]:  # 寻找结束端点
                    fine_partition.append(f)
                    continue
                else:
                    fine_partition.append(f)
            LH  = i - flag  # 计算精细化分区的长度
            LDH = LDH(fine_partition, coarse_partition)
        sum_value = sum_value + LH + LDH
    return sum_value

def Coarse_grained_partition(data, partition):
    """
    按照一定规则对线进行粗粒度划分
    :param data:
    :param partition:粗粒度划分标准对于等于1
    :return:
    """
    # 对线进行划分：等距离取点
    coarse=[]
    for item in range(math.floor(len(data)/partition)):
        coarse.append(data[item])

    if len(data)/partition != 0 :
        coarse.append(data[len(data)])

    return coarse

def mini_value(data):
    greedy_array = []
    for i in np.linspace(1, len(data)-1 ,len(data)-2):
        coarse = Coarse_grained_partition(data, i)  # 获取粗粒度分区
        greedy_array.append(sum_all(data, coarse))  #将最小值放入数组排序
    greedy_array.sort(reverse=False)
    return greedy_array[0]










