from calculate_angle import Calculate
from define import distance_between_T_Partitions
from table_1 import dist
from table_2 import min_vertical, max_l_vertical, minlen, max_angle
from 其他函数 import computer_point
import math


def Judgement_overlap(L_i, L_j):
    k_1, b_1 = computer_point(L_i[0], L_i[1]).define_a_line()
    k_2, b_2 = computer_point(L_j[0], L_j[1]).define_a_line()

    x = (b_2 - b_1) / (k_1 - k_2)
    y = k_1 * x + b_1

    #if dist(L_i, L_j) < D:


    if k_1 == k_2 and b_1 == b_2:
        return "overlap"

    if L_j[0][0] > x > L_i[1][0] and L_i[0][1] > y > L_j[0][1]:
        return "enclose"
    else:
        return "disjoint"


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


def lower_bounds_dist(L_i, L_j, fine):
    """

    :param L_i: 粗线段中的片段
    :param L_j: 粗线段中的片段
    :param fine: 粗线段对应的细精细数据
    :return:
    """
    w_vertical = 1 / 3
    w_parael = 1 / 3
    w_angle = 1 / 3
    return w_vertical * lower_bounds_vertical(L_i, L_j, fine) + \
           w_parael * lower_bounds_parael(L_i, L_j) + \
           w_angle * lower_bounds_angle(L_i, L_j, fine)


def upper_bounds_dist(L_i, L_j, fine):
    """

    :param L_i: 粗线段中的片段
    :param L_j: 粗线段中的片段
    :param fine: 粗线段对应的细精细数据
    :return:
    """
    w_vertical = 0.9
    w_parael = 0.9
    w_angle = 0.9
    return w_vertical * upper_bounds_vertical(L_i, L_j, fine) + \
           w_parael * upper_bounds_parael(L_i, L_j) + \
           w_angle * upper_bounds_angle(L_i, L_j, fine)


def lower_bounds_vertical(L_i, L_j, fine):
    """
    寻找下界
    :param L_i:
    :param L_j:
    :param fine:
    :return:
    """
    min = min_vertical(L_i, L_j)  # 计算端点到直线上投影点对应的最小距离
    max_l_vertical_i = max_l_vertical(L_i, fine)
    max_l_vertical_j = max_l_vertical(L_j, fine)
    return min - max_l_vertical_i - max_l_vertical_j


def upper_bounds_vertical(L_i, L_j, fine):
    """

    :param L_i:
    :param L_j:
    :param fine:
    :return:
    """
    min = min_vertical(L_i, L_j)  # 计算端点到直线上投影点对应的最小距离
    max_l_vertical_i = max_l_vertical(L_i, fine)
    max_l_vertical_j = max_l_vertical(L_j, fine)
    return min + max_l_vertical_i + max_l_vertical_j


def lower_bounds_parael(L_i, L_j):
    judge = Judgement_overlap(L_i, L_j)
    if judge == "enclose" or judge == "overlap":
        return 0
    elif judge == "disjoint":
        return distance_between_T_Partitions(L_i[0][0], L_i[0][1], L_i[1][0], L_i[1][1]).paraller()
    else:
        print("note:error")


def upper_bounds_parael(L_i, L_j):
    judge = Judgement_overlap(L_i, L_j)
    if judge == "enclose":
        if len(L_i) > len(L_j):
            return len(L_i)
        else:
            return len(L_j)

    elif judge == "overlap":
        return len(L_j) + len(L_j) - distance_between_T_Partitions(L_i[0][0], L_i[0][1], L_i[1][0],
                                                                   L_i[1][1]).paraller()
    elif judge == "disjoint":
        return len(L_j) + len(L_j) + distance_between_T_Partitions(L_i[0][0], L_i[0][1], L_i[1][0],                                                            L_i[1][1]).paraller()
    else:
        print("note:error")


def lower_bounds_angle(L_i, L_j, fine):
    if minlen(L_i, fine) > minlen(L_j, fine):
        minlen(L_j, fine) * math.sin(
            Calculate(L_i[0][0], L_i[0][1], L_i[1][0], L_i[1][1]).cos() - max_angle(L_i, fine) - max_angle(L_j, fine))
    else:
        minlen(L_i, fine) * math.sin(
            Calculate(L_i[0][0], L_i[0][1], L_i[1][0], L_i[1][1]).cos() - max_angle(L_i, fine) - max_angle(L_j, fine))


def upper_bounds_angle(L_i, L_j, fine):
    if minlen(L_i, fine) > minlen(L_j, fine):
        minlen(L_j, fine) * math.sin(
            Calculate(L_i[0][0], L_i[0][1], L_i[1][0], L_i[1][1]).cos() + max_angle(L_i, fine) + max_angle(L_j, fine))
    else:
        minlen(L_i, fine) * math.sin(
            Calculate(L_i[0][0], L_i[0][1], L_i[1][0], L_i[1][1]).cos() + max_angle(L_i, fine) + max_angle(L_j, fine))
