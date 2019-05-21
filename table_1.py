#coding:utf-8
from calculate_angle import Point
from define import distance_between_T_Partitions

class table_1():
    def __init__(self, TR_i, TR_j, data):
        self.TR_i = TR_i
        self.TR_j = TR_j
        self.data = data


    def dist(self,L_i, L_j):
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

    def CP(self, TR_i, l_j, D):
        """
        求解：TR_i中小于距离D分区的集合
        分区来自L_j属于TR_j,其中
        L_i属于TR_i的分区并且L_i和L_j的距离小于d(dist(L_i, L_j) < D)
        :param l_j:
        :param TR_j:
        :param D:
        :return:TR_i中小于距离D分区的集合
        """
        set = []  # 存储TR_i中小于距离D分区的集合
        for i in range(len(TR_i) - 1):
            l_i = [TR_i[i], TR_i[i + 1]]
            if l_i == l_j:
                continue
            else:
                if self.dist(l_i, l_j) < D:
                    set.append(l_i)
        return set

    def CTR(self, L_j, D):
        """
        定义一： 定义什么是相互靠经的轨迹--所有L_i属于CP(TR_i, L_j, D)的所有长度len(L_i)大于len(L_j)
        :param L_i:
        :param D:
        :return:
        """
        array = []  # the set of trajectories close to L_i
        set = self.CP(self.TR_j, L_j, D)

        len_j = Point(L_j[0][0], L_j[0][1], L_j[1][0], L_j[1][1]).length()
        for l_i in set:
            len_i = Point(l_i[0][0], l_i[0][1], l_i[1][0], l_i[1][1]).length()
            if len_i >= len_j:
                array.append(l_i)  #
        return array


    def density(self, L_j, CL, CL_index):
        """
        L_i的密度
        :param L_i:
        :return:
        """
        # array = []
        # for TR_i in self.data:
        #     item = self.CP(TR_i[1], L_j, 55)
        #     array.append(item)
        # return len(array)
        for i, j in enumerate(CL_index):
            if L_j == j:
                return len(CL[i])
            else:
                return 1

    def adj(self, L_i, CL_i, CL_j, CL_i_index, CL_j_index):
        sum = 0.0
        for length, TR_j in enumerate(self.data):
            for i in range(len(TR_j[1])-1):
                L_j = [TR_j[1][i], TR_j[1][i + 1]]
                sum += self.density(L_j, CL_i, CL_i_index)

        density_j = sum/length
        return density_j / self.density(L_i, CL_j, CL_j_index)

    def Ofrac(self, TR_i):
        sum = 0.0
        for item in TR_i:
            sum += Point(item[0][0], item[0][1], item[1][0], item[1][1]).length()
        sum_2 = 0.0
        for it in range(len(self.TR_i[1])-1):
             sum_2 += Point(self.TR_i[1][it][0], self.TR_i[1][it][1], self.TR_i[1][it+1][0], self.TR_i[1][it+1][1]).length()

        return sum/sum_2


