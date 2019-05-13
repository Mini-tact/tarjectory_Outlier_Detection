"""
轨迹异常值检测
"""
from 细粒度划分 import lower_bounds_dist, upper_bounds_dist
from 读取数据 import getData

if __name__ == "__main__":
"""
数据划分部分
"""
# 定义超参
D = 85
p = 0.95
F=0.2
CL_i = []
CL_j = []
# 数据划分
data = getData()
# 在粗糙路径数据集中两两配对寻找边缘路径
for item in data:
    for i in len(item[0])-1:
        L_i=[item[i], item[i+1]]  # 取粗线段中的线段
        for j in item[0]:
            L_j = [item[j], item[j + 1]]  # 取粗线段中的线段
            if  L_i == L_j: # 寻找两个data几何中不相同的两条路径 L_i_l,L_j_l中存放的是粗线段的片段和对应的精细化片段
                continue
            else:
                # relu 1
                if lower_bounds_dist(L_i, L_j, item[1]) > D:
                    continue
                else:
                    # 在精准粒度中分区L_i和L_j
                    pass
                # relu 2
                if upper_bounds_dist(L_i, L_j, item[1]) <= D:
                    # 进入此循环，则说明L_i和L_j相互靠近，将他们的精细分区分别存入数据集中
                    fine_partition_part = item[item.index(L_i[0]), item.index(L_i[1]) + 1]
                    fine_partition_part = item[item.index(L_j[0]), item.index(L_j[1]) + 1]
                    CL_i.append(L_j)
                    CL_j.append(L_i)
                else:
                    # Every pair of fine t-partitions is compared
                    for l_i in CL_i:
                        for l_j in CL_j:
                            # 计算dist(l_i, l_j)
                            if dist(l_i,l_j) <= D:

                            else:








    #
