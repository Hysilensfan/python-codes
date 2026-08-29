# First method
def recurtion(w: int) -> int:
    t: int = 1
    if w != 0 and w!= 1:
        for i in range(1, w + 1):
            t *= i
        return t
    else:
        return 1


for _ in range(int(input())):
    c: int = int(input())
    print(recurtion(c))

# Second method
recurtion = lambda w:  w * recurtion(w-1) if w != 0 else 1

[print(recurtion(int(input()))) for _ in range(int(input()))]

# Third method
from math import factorial as f

[print(f(int(input()))) for _ in range(int(input()))]
