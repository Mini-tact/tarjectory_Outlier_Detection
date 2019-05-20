from calculate_angle import Calculate, Point
from other import computer_point
import math

class distance_between_T_Partitions():
    """
           两个t-partitions之间的距离
           三个部分组成
           A.垂直距离
           B.平行距离
           C.两条线之间的夹角
           :param s_i: L_i的起始点
           :param e_i: L_i的终点
           :param s_j: L_j的起始点
           :param e_j: L_j的起始点
    """
    def __init__(self, s_i, e_i, s_j, e_j):
        self.s_i = s_i
        self.e_i = e_i
        self.s_j = s_j
        self.e_j = e_j




    def perpendicular(self):
        """
        计算垂直距离
        垂直距离定义为： L_j的端点到L_i的映射点之间距离的平方和除以L_j的端点到L_i的映射点之间距离和
        """
        l_1 = computer_point(self.s_i, self.e_i).D_form_point_to_line(self.s_j)
        l_2 = computer_point(self.s_i, self.e_i).D_form_point_to_line(self.e_j)
        return (math.pow(l_1, 2)+math.pow(l_2, 2))/(l_1+l_2)

    def paraller(self):
        """
        L_j在L_i上的映射点到L_i 2个端点的距离的最小值
        :return:
        """
        #computer_point(self.s_i, self.e_i).Perpendicular_to_a_point(self.s_j)  # 计算s_j在Li上的垂线
        #computer_point(self.s_i, self.e_i).Perpendicular_to_a_point(self.e_j)  # 计算e_j在Li上的垂线
        # cosa*对边等于 映射点到点的距离

        # L_i[0], L_i[1], L_j[0], L_j[1]
        #Calculate(L_i[0], L_i[1], L_j[0], L_j[1]).cos()
        #s_j_cos_ei = Calculate(self.e_i, self.s_j, self.e_i, self.s_i).cos()*Point(self.e_i[0], self.e_i[1], self.s_j[0],self.s_j[1]).length()
        s_j_cos_si = Calculate(self.s_i, self.s_j, self.s_i, self.e_i).cos() * Point(self.s_i[0], self.s_i[1],self.s_j[0], self.s_i[1]).length()

        e_j_cos_ei = Calculate(self.e_i, self.e_j, self.e_i, self.s_i).cos()*Point(self.e_i[0], self.e_i[1], self.e_j[0],self.e_j[1]).length()
        #e_j_cos_si = Calculate(self.s_i, self.e_j, self.s_i, self.s_i).cos() * Point(self.s_i[0], self.s_i[1],self.e_j[0],self.s_i[1]).length()

        if s_j_cos_si > e_j_cos_ei:
            return e_j_cos_ei
        else:
            return s_j_cos_si

    def angle_distance(self):
        """
        计算角距离
        :return:
        """
        L_j = Point(self.s_j[0], self.s_j[1], self.e_j[0], self.e_j[1]).length()
        angle = Calculate(self.s_i, self.e_i, self.s_j, self.e_j).cos()
        if angle > 0:
            # 角度在0~90之间
            angle = angle - pow(10,-10)   #防止数据溢出
            return L_j*math.sqrt(1.0000000-math.pow(angle, 2))# ||L_j*sin||
        else:
            return L_j
















