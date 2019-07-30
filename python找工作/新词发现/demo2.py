import numpy as np


def calc_ent(x):
    x_value_list = set([x[i] for i in range(x.shape[0])])
    ent = 0.0
    for x_value in x_value_list:
        p = float(x[x == x_value].shape[0]) / x.shape[0]
        log_p = np.log2(p)
        ent -= p * log_p

    return ent
def calc_condition_ent(x, y):
    # calc ent(y|x)
    x_value_list = set([x[i] for i in range(x.shape[0])])
    ent = 0.0
    for x_value in x_value_list:
        print(x_value)
        sub_y = y[x == x_value]
        # print(sub_y)
        temp_ent = calc_ent(sub_y)
        print(temp_ent)
        # print(sub_y.shape[0])
        # print(y.shape[0])
        ent += (float(sub_y.shape[0]) / y.shape[0]) * temp_ent

    return ent
x=np.array([2,2,2,3,3,4,4,4,4,6,6])
# y=[x == 2]
# print(y)
y=np.array([1,1,1,2,2,2,2,2,2,1,1])
# y=np.array([1,1,1,2,2.1])
print(calc_condition_ent(x,y))