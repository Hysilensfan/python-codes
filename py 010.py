#first method
a , b , c = [int(x) for x in input().split()]
"""
Line 2 equal below code:
a: int = int(a)
b: int = int(b)
c: int = int(c)
# a, b, c = input().split()

"""
v: int = b ** 2 - a * c * 4
ans: str = "NoSolution"
if v == 0:
    ans: str = f"DR={b / (-2*a)}"
elif v > 0:
    ans: str = f"{(-b - v ** 0.5) / (2 * a)} {(-b + v ** 0.5) / (2 * a)}"
print(ans)
# second method
from math import sqrt  # "sqrt" calculates the real square root (with decimals);"isqrt" calculates only the integer part, directly discarding the decimals!

f = lambda a, b, c:b ** 2 - a * c * 4

v: int = f(*map(int, input().split()))
print(f"DR={b / (-2 * a)}" if v == 0 else f"{(-b - sqrt(v)) / (2 * a)} {(-b + sqrt(v)) / (2 * a)}" if v > 0 else "NoSolution")  # Ternary operator.
