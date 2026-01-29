def f(w):
    t=0
    a=1
    for i in range(1, w+1):
        a=a*i;t+=a;t=int(str(t)[-6:])
    return t
for i in range(int(input())):
    w=int(input());r = f(w);v = len(r)
    if v < 7:
        v = r.zfill(6)
    print(f(w))
