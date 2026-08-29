for _ in range(int(input())):
    n: str = input()
    tot: int = 0
    count_O: int = 0
    for c in n:
        if c == 'O':
            tot += 1 + count_O
            count_O += 1
        else:
            count_O = 0
    print(tot)
