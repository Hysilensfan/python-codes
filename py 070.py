def report(v):
    r, k = '', 0
    while k < len(v):
        c, n = v[k], 0
        k += 1
        while k < len(v) and v[k].isdigit():
            n = n * 10 + int(v[k])
            k += 1
        r += n * c
    return r


[print(report(input())) for _ in range(int(input()))]
