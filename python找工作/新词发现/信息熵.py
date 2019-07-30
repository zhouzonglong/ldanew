import numpy as np

'''
计算信息熵：H(x)=E（p*log（p））
:param x:      np.arry()
:return:       float E

example:
[2,2,2,3,3,1]
x[x == x_value]--->[2,2,2],[3,3],[1]

'''
def calc_ent(x):

    x_value_list = set([x[i] for i in range(x.shape[0])])
    ent = 0.0
    for x_value in x_value_list:
        p = float(x[x == x_value].shape[0]) / x.shape[0]
        log_p = np.log2(p)
        ent -= p * log_p

    return ent
"""
    条件熵   H(Y|X)=E（p(x,y)*H(Y|X=x)）=E{p(x,y)*E[p(y|x)*log(p(y|x))]}
                   =-E(p(x,y)*log p(y|x))
    
    calculate ent H(y|x)
"""
def calc_condition_ent(x, y):
    # calc ent(y|x)
    x_value_list = set([x[i] for i in range(x.shape[0])])
    ent = 0.0
    for x_value in x_value_list:
        sub_y = y[x == x_value]
        temp_ent = calc_ent(sub_y)
        ent += (float(sub_y.shape[0]) / y.shape[0]) * temp_ent

    return ent
"""
        信息增益:==熵---条件熵
        ent_prap = H(Y) - H(Y|X)
"""
def calc_ent_grap(x,y):


    base_ent = calc_ent(y)
    condition_ent = calc_condition_ent(x, y)
    ent_grap = base_ent - condition_ent

    return ent_grap
'''
点互信息
pMI(x,y)=log(p(x,y)/(px*py))
'''
x=[2,2,2,3,3,1]
print(calc_ent(np.array(x)))

