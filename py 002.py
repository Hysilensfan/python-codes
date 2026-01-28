#first compose method
r = float(input());print(f"{r**2*3.14} {r*2*3.14}"if r>0 else "Wrong")
#second compose method
from math import pi;s = lambda r:f"{r**2*(int(pi*100)/100)} {r*2*(int(pi*100)/100)}"if r>0 else "Wrong";print(s(float(input()))) #the r=s(float(input()) in function s(r) short for s(float(input()));if u input"5",the output will has deviation
