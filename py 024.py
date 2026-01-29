def f(w):
    t = 0;a = 1
    for i in range(1, w + 1):
        a *= i;t = (t + a) % 1000000
    return t
for i in range(int(input())):
    w = int(input());r = str(f(w));
    if len((r)) < 6:r = r.zfill(6)
    print(r)
