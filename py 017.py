#first method
for _ in range(int(input())):
    s: int = int(input())
    t: bool = True
    if s < 2:
        t: bool = False
    else:
        for i in range(2, int(s**0.5) + 1): #using the square root for save calculation times,because this problem descripition that can only  be calculated in 1 second
            if s % i == 0:
                t: bool = False
                break
    print("Y" if t else"N")
#second method
def f(s):
    if s < 2:
        return False
    else:
        for i in range(2, int(s**0.5) + 1):
            if s % i == 0:
                return False
                break
        return True


for _ in range(int(input())):
    print("Y" if f(int(input())) else"N")
#third method
from math import sqrt
f = lambda s:s > 1 and all(s % i != 0 for i in range(2, int(sqrt(s)) + 1))  #lamda belike define function.any Determine if an object is iterable and check if one of its elements is True.
[print("Y" if f(int(input())) else"N") for _ in range(int(input()))]
