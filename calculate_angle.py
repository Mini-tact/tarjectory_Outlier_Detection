import math
import numpy as np

# 得到向量的坐标以及向量的模长
class Point(object):
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def vector(self):
        c = (self.x1 - self.x2, self.y1 - self.y2)
        return c

    def length(self):
        d = math.sqrt(pow((self.x1 - self.x2), 2) + pow((self.y1 - self.y2), 2))
        return d

class Calculate(object):
    def __init__(self, l1s, l1e, l2s, l2e):
        self.l1s = l1s  # 直线1开始坐标
        self.l1e = l1e  # 直线1的结束坐标
        self.l2s = l2s
        self.l2e = l2e


    def Vector_multiplication(self):
        """
        矢量乘法
        :return:
        """
        l1_vector = Point(self.l1s[0], self.l1s[1], self.l1e[0], self.l1e[1]).vector()
        l2_vector = Point(self.l2s[0], self.l2s[1], self.l2e[0], self.l2e[1]).vector()
        return np.dot(l1_vector, l2_vector)

    def the_product_of_mold(self):
        l1_len = Point(self.l1s[0], self.l1s[1], self.l1e[0], self.l1e[1]).length()
        l2_len = Point(self.l2s[0], self.l2s[1], self.l2e[0], self.l2e[1]).length()
        if l1_len == 0.0:
            print(self.l1s+self.l1e)
            print('the length of l1_len is zero')
        elif l2_len == 0.0:
            print(self.l2s+self.l2e)
            print('the length of l2_len is zero')
        else:
            pass
        return l1_len*l2_len

    def cos(self):
        cos = self.Vector_multiplication()/self.the_product_of_mold()
        if cos < 0:  # 求互余角
            cos = - math.sqrt(1 - math.pow(cos, 2))
        return cos

    def angle(self):
        math.acos(self.cos())