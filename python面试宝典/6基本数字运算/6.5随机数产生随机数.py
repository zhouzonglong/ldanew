import random

def rand5():
    return random.randint(1,5)
def rand5_7():
    while True:
        sum=rand5()*5+rand5()
        if sum>=21:
            continue
        return sum%7+1



def rand7():
    # return int(random.random(1,6))
    return random.randint(1,7)
def rand7_10():
    x=0
    while True:
        x=(rand7()-1)*7+rand7()
        if x>40:
            continue
        else:
            return x%10+1

def test_rand7_10():
    i=0
    list=[0]*10
    # print(list)
    while i<10000:
        x=rand7_10()
        list[x]+=1
        # if x%100==0:
            # print('------------'+str(i))
        i+=1
    print(list)
for i in range(5):
    test_rand7_10()