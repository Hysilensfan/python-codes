# First method
gcd = lambda a, b: gcd(b, a % b) if a % b != 0 else b
lcm = lambda f, g: f * g // gcd(f, g)


for _ in range(int(input())):
    d: list = list(map(int, input().split(',')))
    c = l = d[0]
    for e in d[1:]:
        c: int = gcd(c, e)
        l: int = lcm(l, e)
    print(f"{c} {l}")

# Second method
from math import gcd as g_
from math import lcm as l

for _ in range(int(input())):
    d: list[int] = list(map(int, input().split(',')))
    print(g_(*d), l(*d))
