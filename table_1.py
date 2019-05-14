from define import distance_between_T_Partitions


def dist(L_i, L_j):
    dbtp = distance_between_T_Partitions(L_i[0], L_i[1], L_j[0], L_j[1])
    # 在文章中提到权重的大小取决于具体的应用，但是文章没有讲到到底如何选择，因此，此处的权重都为1/3
    weight_vectical = 1/3  # 垂直的权重、
    weight_parael = 1 / 3
    weight_angle = 1 / 3
    return dbtp.perpendicular()*weight_vectical*dbtp.paraller()*weight_parael+dbtp.angle_distance()*weight_angle


def adj(L_i):
    return 0
def CTR(L_i, D):
    return 0

def Ofrac(TPR_i):
    return 0
