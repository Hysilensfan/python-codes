# First method
for _ in range(int(input())):
    b1, b2 = [input() for _ in range(2]
    d: int = 0
    for i in range(len(b1)):
        d += 1 if b1[i] != b2[i] else 0
    print(d)

# Second method
[print(bin(int(input(),2) ^ int(input(),2)).count("1"))for k in range(int(input()))]
