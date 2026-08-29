# First method
def gcd(a: int, b: int) -> int:
    r: int = a % b
    return gcd(b, r) if r != 0 else b


for _ in range(int(input())):
    d = list(map(int, input().split(',')))
    c = d[0]
    for e in d[1:]:
        c = gcd(c, e)
    print(c)

# Second method
from math import gcd

[gcd(*map(int, input().split(','))) for _ in range(int(input()))]
