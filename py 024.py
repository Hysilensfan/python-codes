#first method
def f(w):
    t = 0;a = 1
    for i in range(1, w + 1):
        a *= i;t = (t + a) % 1000000
    return t
for i in range(int(input())):
    w = int(input());r = str(f(w));print( '0' * (6 - len(r)) + r if len((r))<6 else r )
#second method
f = lambda w, a=1, t=0: ([t := (t + (a := a * i)) % 1000000 for i in range(1, w+1)] and t) # commas here only split parameters, not like ; that separates multiple statements.by the way, here "and" does not for logical operationit means the list had a value,so t is returned
for _ in range(int(input())): r=str(f(int(input())));print(r:=r.zfill(6) if len(r)<6 else r)
