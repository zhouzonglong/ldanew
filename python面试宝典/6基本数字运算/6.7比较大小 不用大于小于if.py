#  |a-b|==a-b  则a》b
def max_ab(a,b):
    return abs(a-b)==(a-b)
    # return ((a+b)+abs(a-b)/2)
print(max_ab(5,6))
