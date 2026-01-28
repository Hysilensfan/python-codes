for _ in range(int(input())):
    b1 = input();b2 = input();d = 0
    for i in range(len(b1)):
        d += 1 if b1[i] != b2[i] else 0
    print(d)
