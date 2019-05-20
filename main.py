"""
轨迹异常值检测
"""
import math

from table_1 import table_1
from fine import lower_bounds_dist, upper_bounds_dist
from read_data import getData


if __name__ == "__main__":
    """
    数据划分部分
    """
    # 定义超参
    D = 55
    p = 0.95
    F = 0.2
    CL_i = {}  # 存放的是一个片段，不是一个点
    CL_j = {}
    outlying = []  # 存放异常值
    outlying_fine = []  # 存放异常值的整条线段
    # 数据划分
    data = getData()
    # 在粗糙路径数据集中两两配对寻找边缘路径
    print("---------------------------------数据读取完成，进入划分模块---------------------------------")
    for number, item in enumerate(data):
        for i in range(len(item[0])-1):
            L_i = [item[0][i], item[0][i + 1]]  # 取粗线段中的线段
            CL_j[number] = L_i
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
                        CL_i[number] = l_j
                        #CL_j[j] = l_i
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
                                if table_1(0, 0, 0).dist(l_i, l_j) <= D:
                                    CL_i[number] = l_j

    print("线段与数字对应的坐标为")
    print(CL_j)
    print("线段对应的靠近的线段")
    print(CL_i)

    """
    Detection Phase
    F 表示精细划分数据集
    """
    print("----------------------------detection------------------------------")
    F = data  # the set of fine t-partition
    for i, TR_i in enumerate(F):
        for j, TR_j in enumerate(F):
            print('求解轨迹'+str(i)+'和轨迹'+str(j))
            if TR_i[1] == TR_j[1]:  # 寻找两个data几何中不相同的两条路径 L_i_l,L_j_l中存放的是粗线段的片段和对应的精细化片段
                continue

            for i in range(len(TR_i[1])-1):
                l_i = [TR_i[0][i], TR_i[0][i + 1]]
                # count CRT(l_i,D)
                crt_value = len(table_1(TR_i[1], TR_j[1], data).CTR(l_i, D))
                # judge
                if math.ceil(crt_value * table_1(TR_i[1], TR_j[1], data).adj(l_i)) <= math.ceil((1 - p)*len(l_i)):  # 判断是否为异常值
                    outlying.append(l_i)
                    print(l_i)

        if table_1(TR_i, 0, 0).Ofrac(outlying) >= F:
            # Output TR_i with its outlying fine t-partitions:
            outlying_fine.append(TR_i)
            print(outlying_fine)
        print('----------------next-------------------------')
    # end




