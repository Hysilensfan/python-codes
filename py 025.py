def f(w):
    a=1
    for i in range(2, w+1):
        a=int(str(a*i).rstrip('0'))%100000 # When calculating factorials, first remove the zeros, then keep only the last 5 digits.Reduce execution times
    return a
for i in range(int(input())):
    w=int(input());v=str(f(w))
    for e in range(len(v)-1,-1,-1):
        if v[e]!='0':
            print(v[e])
            break
