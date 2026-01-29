#first method
n = int(input());print(f"{n//100} {(n%100)//10} {n%10}" if 1<=n<=999 else "Wrong") #semicolon separates statements; hint:123//100=1;123%100=23,23//10=2;123%10=3
#second method
from sys import stdin as f;s=int(f.readline());print("{} {} {}".format(s//100,(s%100)//10,s%10)if 1<=s<=999 else "wrong")
