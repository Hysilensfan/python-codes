#first method
r = float(input());print(f"{r**2*3.14} {r*2*3.14}"if r>0 else "Wrong")
#second method
from math import pi;s = lambda r:f"{r**2*(int(pi*100)/100)} {r*2*(int(pi*100)/100)}"if r>0 else "Wrong";print(s(float(input()))) #s(r) is called with float(input())
