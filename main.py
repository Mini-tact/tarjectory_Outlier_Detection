"""
轨迹异常值检测
"""
import math
from table_1 import dist, adj, Ofrac, CTR
from 细粒度划分 import lower_bounds_dist, upper_bounds_dist
from 读取数据 import getData


if __name__ == "__main__":
    """
    数据划分部分
    """
    # 定义超参
    D = 85
    p = 0.95
    F = 0.2
    CL_i = []  # 存放的是一个片段，不是一个点
    CL_j = []
    outlying = []  # 存放异常值
    outlying_fine = []  # 存放异常值的整条线段
    # 数据划分
    data = getData()
    # 在粗糙路径数据集中两两配对寻找边缘路径
    print("---------------------------------数据读取完成，进入划分模块---------------------------------")
    for item in data:
        for i in range(len(item[0])-1):
            L_i = [item[0][i], item[0][i + 1]]  # 取粗线段中的线段
            for j in range(len(item[0])-1):
                L_j = [item[0][j], item[0][j + 1]]  # 取粗线段中的线段
                if (L_i[0] == L_j[0]) and L_i[1] == L_j[1]:  # 寻找两个data几何中不相同的两条路径 L_i_l,L_j_l中存放的是粗线段的片段和对应的精细化片段
                    pass
                else:
                    # relu 1
                    if lower_bounds_dist(L_i, L_j, item[1]) > D:
                        continue
                    else:
                        # 在精准粒度中分区L_i和L_j
                        pass
                    # relu 2
                    if upper_bounds_dist(L_i, L_j, item[1]) <= D:
                        """
                        进入此循环，则说明L_i和L_j相互靠近，将他们的精细分区分别存入数据集中
                        CL（l_i）holds the t-partitions close to l_i
                        所有l_i属于L_i and l_j属于L_j
                        Insert l_i into CL(l_j) and l_j into CL(l_i)
                        
                        item[0] 存储的粗划分
                        item[1] 存储的是细化分
                        """
                        l_i = item[1][item[0].index(L_i[0]):item[0].index(L_i[1]) + 1]
                        l_j = item[1][item[0].index(L_j[0]):item[0].index(L_j[1]) + 1]
                        CL_i.append(l_j)
                        CL_j.append(l_i)

                    else:
                        """
                        计算的为每个粗分区对应的细分区的所有点
                        """
                        array_1 = item[1][item[0].index(L_i[0]):(item[0].index(L_i[1]) + 1)]  # 点坐标
                        array_2 = item[1][item[0].index(L_j[0]):(item[0].index(L_j[1]) + 1)]
                        for i in range(len(array_1) - 1):
                            l_i = [array_1[i], array_1[i + 1]]  # 取粗线段中的线段
                            for j in range(len(array_2) - 1):
                                l_j = [array_2[j], array_2[j + 1]]  # 取粗线段中的线段
                                # 计算dist(l_i, l_j)
                                if dist(l_i, l_j) <= D:
                                    CL_i.append(l_j)   # insert l_i into CL(l_j) and l_j into CL(l_i)
                                    CL_j.append(l_i)
    """
    Detection Phase
    F 表示精细划分数据集
    """
    print("----------------------------detection------------------------------")
    # count math.ceil(CTR(l_i,D))by using CL_i
    F = data[1]  # the set of fine t-partition
    for l_i in F:
        # count CRT(l_i,D)
        crt_value = abs(CTR(l_i, D))
        # judge
        if math.ceil(crt_value*adj(l_i)) <= math.ceil((1-p)*len(l_i)):  # 判断是否为异常值
            outlying.append(l_i)

    # Output TR_i with its outlying fine t-partitions:
    for TR_i in data[1]:
        if Ofrac(TR_i) >= F:
            outlying_fine.append(TR_i)

    # end




