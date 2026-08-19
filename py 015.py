#first method
for i in range(int(input())):
    e: int = int(input())
    tot, ope, k = 3, 1, 2
    if e > 1:
        for p in range(e - 1):
            if ope == 1:
                tot += 4 / (k * (k + 1) * (k + 2))
                ope = 0
            elif ope == 0:
                tot -= 4 / (k * (k + 1) * (k + 2))
                ope = 1
            k += 2
    print(tot)
