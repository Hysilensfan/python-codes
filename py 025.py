# First method
def f(w):
    a: int = 1
    for i in range(2, w+1): # hypothesis input(w) is 1 this row won't operation so output 1(default value of a)
        a: int = (a * i) % 100000 # When calculating factorials, first remove the zeros, then keep only the last 5 digits.Reduce execution times
    return a


for i in range(int(input())):
    w: int = int(input())
    v: str = str(f(w))
    for e in range(len(v)-1, -1, -1):
        if v[e] != '0':
            print(v[e])
            break

# Second method
from math import factorial as fac


def not_zero(d: int) -> int:
    for i in str(d)[::-1]:
        if int(i) != 0:
            return int(i)
    return 0  # In normal execution, this will return an integer.


[print(not_zero(fac(int(input())))) for _ in range(int(input()))]

