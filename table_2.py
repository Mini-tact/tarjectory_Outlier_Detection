from calculate_angle import Point, Calculate
from 其他函数 import computer_point

def max_l_vertical(L_i, fine):
    """
    L_i中的粗线段片段和对应精细片段的最大的垂直距离
    :param L_i:
    :param L_j:
    :param fine:
    :return:
    """
    fine_partition_part=fine[fine.index(L_i[0]), fine.index(L_i[1])+1]
    result= []
    for l_i in fine_partition_part:
        result.append(computer_point(L_i[0], L_i[1]).D_form_point_to_line(l_i))
    result.sort(reverse=False) # 从大到小排序
    return result[0]

def minlen(L_i, fine):
    """
    计算粗线段L_i对应的精细线段中的所有精细分区的最小值
    :param L_i:
    :param fine:
    :return:
    """
    fine_partition_part = fine[fine.index(L_i[0]), fine.index(L_i[1]) + 1] #  获取粗线段对应的精细线段
    result=[]
    for i in range(len(fine_partition_part)-1):
        length = Point(fine_partition_part[i][0],
                      fine_partition_part[i][1],
                      fine_partition_part[i+1][0],
                      fine_partition_part[i+1][1],
                      ).length() # 获取粗线段对应的精细片段中的每个分区线段,并计算长度
        result.append(length)
    result.sort()
    return result[0]

def maxlen(L_i, fine):
    """
    计算粗线段L_i对应的精细线段中的所有精细分区的最大值
    :param L_i:
    :param fine:
    :return:
    """
    fine_partition_part = fine[fine.index(L_i[0]), fine.index(L_i[1]) + 1] #  获取粗线段对应的精细线段
    result=[]
    for i in range(len(fine_partition_part)-1):
        length = Point(fine_partition_part[i][0],
                      fine_partition_part[i][1],
                      fine_partition_part[i+1][0],
                      fine_partition_part[i+1][1],
                      ).length() # 获取粗线段对应的精细片段中的每个分区线段,并计算长度
        result.append(length)
    result.sort(reverse=False)
    return result[0]

def max_angle(L_i, fine):
    result = []
    fine_partition_part = fine[fine.index(L_i[0]), fine.index(L_i[1]) + 1]  # 获取粗线段对应的精细线段
    for i in range(len(fine_partition_part)-1):
        angle = Calculate(L_i[0], L_i[1],fine_partition_part[i], fine_partition_part[i+1]).cos()
        result.append(angle)
    result.sort(reverse=False)
    return result[0]

def min_vertical(coarse_t, point_1, point_2):
    """
    计算端点到直线上投影点对应的最小距离
    :param coarse_t: 粗线段上的分区，两个端点
    :param point: 细线段上的点
    :return:
    """
    l_1 = computer_point(coarse_t[0], coarse_t[1]).D_form_point_to_line(point_1)
    l_2 = computer_point(coarse_t[0], coarse_t[1]).D_form_point_to_line(point_2)

    if l_1>l_2:
        return l_2
    else:
        return l_1

def angle():
    return 0
