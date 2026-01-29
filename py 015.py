#first method
for i in range(int(input())):
    s = int(input());j = 2;pi = 3;plus = True
    for i in range(s - 1):
        k = (4 / (j * (j + 1) * (j + 2)))
        if plus:
            pi += k
        else:
            pi -= k
        j += 2
        plus = False
    print(pi)
#second method
for _ in range(int(input())):
    s = int(input());pi = 3;j = 2;plus = lambda: True
    for _ in range(s - 1):k = 4 / (j * (j + 1) * (j + 2));pi += k if plus() else -k;j += 2; plus = lambda: not plus()
    print(pi)
