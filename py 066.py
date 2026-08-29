for _ in range(int(input())):
    N: str = (bin(int(input()))).replace("0b", "")
    tot: int = 0
    for c in range(len(N)):
        if N[c] == '1':
            tot += 1
    print(tot)
