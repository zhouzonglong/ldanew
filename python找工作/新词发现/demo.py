import numpy as np
n=4
def cut(s):
    # print('-----------------------------------')
    r = np.array([0]*(len(s)-1))
    # print(s)
    # print(r)
    for i in range(len(s)-1):
        for j in range(2, n+1):
            print(s[i:i+j])
            if s[i:i+j] in {'老师': 2, '前年': 7, '在': 4, '西天': 4}:
                print(r)
                r[i:i+j-1]+=1
                print(r)


    w = [s[0]]

    for i in range(1, len(s)):

        if r[i-1] > 0:
            # print(w)
            w[-1] += s[i]
            # print(w)
            # print('--------------------')
        else:
            w.append(s[i])
    print(w)
    print(r)
    return w
cut('老师父可是前年过此河往西天取经的')