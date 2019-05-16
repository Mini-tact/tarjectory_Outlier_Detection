from calculate_angle import Point
from define import distance_between_T_Partitions


def dist(L_i, L_j):
    """
    求两个线段之间的距离
    :param L_i: 线段
    :param L_j: 线段
    :return:
    """
    dbtp = distance_between_T_Partitions(L_i[0], L_i[1], L_j[0], L_j[1])
    # 在文章中提到权重的大小取决于具体的应用，但是文章没有讲到到底如何选择，因此，此处的权重都为1/3
    weight_vectical = 1/3  # 垂直的权重
    weight_parael = 1 / 3
    weight_angle = 1 / 3
    return dbtp.perpendicular()*weight_vectical+dbtp.paraller()*weight_parael+dbtp.angle_distance()*weight_angle

def CP(TR_i, L_j, D):
    """
    求解：TR_i中小于距离D分区的集合
    分区来自L_j属于TR_j,其中
    L_i属于TR_i的分区并且L_i和L_j的距离小于d(dist(L_i, L_j) < D)
    :param TR_i:
    :param L_j:
    :param D:
    :return:TR_i中小于距离D分区的集合
    """
    set = []  # 存储TR_i中小于距离D分区的集合
    for i in range(len(TR_i)-1):
        L_i = [TR_i[i], TR_i[i+1]]
        if dist(L_i, L_j) < D:
            set.append(L_i)
    return set

def CTR(TR_i, L_j, L_i, D):
    """
    定义一： 定义什么是相互靠经的轨迹--所有L_i属于CP(TR_i, L_j, D)的所有长度len(L_i)大于len(L_j)
    :param L_i:
    :param D:
    :return:
    """
    array = []  # the set of trajectories close to L_i
    set = CP(TR_i, L_j, D)

    len_i = 0.0
    for l_i in set:
        len_i += Point(l_i[0][0], l_i[0][1], l_i[1][0], l_i[1][1]).length()
    len_j = Point(L_j[0][0], L_j[0][1], L_j[1][0], L_j[1][1]).length()
    if len_i >= len_j:
        array.append(l_i)  # 此处可能有错！！！！！！！！！！！！！！！！！！！！！
    return array

def adj(L_i):

    return 0


def Ofrac(TPR_i):
    return 0
