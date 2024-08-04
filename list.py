def fun(inp):
    l = []
    for i in range(len(inp)):
        if i == len(inp) - 1: 
            l.append(inp[i] * i + inp[0])
        else:
            l.append(inp[i] * i + inp[i+1])
    return l
inp = list(map(int,input().split()))
print(fun(inp))