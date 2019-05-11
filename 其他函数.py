import math
class computer_point():
    def __init__(self, s, e):
        self.s = s
        self.e = e

    def define_a_line(self):
        """
        两个点确定一条直线
        :return: 返回K和截距
        """
        # 计算斜率
        k = (self.s[0] - self.e[0])/(self.s[1] - self.e[1])
        # 计算截距
        b = self.e[0]-k*self.s[0]
        return k, b

    def D_form_point_to_line(self, point):
        """
        计算点到直线的距离
        :param point: 点
        :return: 返回点到直线的距离
        """
        k, b = self.define_a_line()
        return (-k*point[0] + point[1]-b)/math.sqrt(math.pow(k, 2)+1)

    def Perpendicular_to_a_point(self, point):
        # 计算直线方程
        k, b = self.define_a_line
        # 计算过某点的垂线
        k = -1/k
        b = point[1] - k*point[0]
        return k, b




