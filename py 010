#first compose method
from math import isqrt
def f(a,b,c):
    return b**2-a*c*4
a , b , c = map(int, input().split());v = f(a,b,c);ans = "NoSolution"
if v == 0:
    ans = f"DR={b/(-2*a)}"
elif v > 0:
    ans = f"{(-b-isqrt(v))/(2*a)} {(-b+isqrt(v))/(2*a)}"
print(ans)
#second compose method
a , b , c = input().split();a = int(a);b = int(b);c = int(c);v = b**2 - a * c *4;ans = "NoSolution"
if v == 0:
    ans = f"DR={b/(-2*a)}"
elif v > 0:
    ans = f"{(-b-v**0.5)/(2*a)} {(-b+v**0.5)/(2*a)}"
print(ans)
