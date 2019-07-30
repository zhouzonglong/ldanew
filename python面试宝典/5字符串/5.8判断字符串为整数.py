def ifint(strs):
    try:
        n=int(strs)
        print(n)
    except:
        print('strs不是int')
ifint('++88')
