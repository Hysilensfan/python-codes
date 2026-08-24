# First method
def factorial(x):
    tot: int = 0
    for c in range(1, x + 1):
        h: int = 1
        for i in range(1, c + 1):
            h *= i
        tot = (tot + h) % 1000000
    return str(tot).zfill(6)


for k in range(int(input())):
    print(factorial(int(input())))

# Second method
recurtion = lambda w: w * recurtion(w - 1) if w != 0 else 1


def factorial(r):
    tot = 1
    if r == 1:
        return "000001"
    elif r == 22 or r >= 24:
        return "940313"
    elif 24 > r > 1:
        if r > 1:
            while r > 1:
                tot = (tot + recurtion(r)) % 1000000
                r -= 1
        return str(tot).zfill(6)


[print(factorial(int(input()))) for _ in range(int(input()))]

# Third method
f = lambda w, a = 1, t = 0: ([t := (t + (a := a * i)) % 1000000 for i in range(1, w + 1)] and t) # commas here only split parameters, not like ; that separates multiple statements.by the way, here "and" does not for logical operationit means the list had a value,so t is returned
for _ in range(int(input())):
    r: str = str(f(int(input())))
    print(r := r.zfill(6) if len(r) < 6 else r)
