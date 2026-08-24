# First method
def happy(s: int):
    n: set = set()
    while s != 1:
        if s in n:
            break
        n.add(s)
        t = 0
        for e in range(len(str(s))):  # Digit sum.
            t += int(str(s)[e]) ** 2
        s = t
    else:
        return True
    return False


for i in range(int(input())):
    print("T" if happy(int(input())) else"F")

# Second method
def isHappy(self, n: int) -> bool:
    dire: set = set()
    while n != 1 and n not in dire:
        dire.add(n)
        n: int = sum(int(c) ** 2 for c in str(n))
    return n == 1


[print("T" if happy(int(input())) else"F") for _ in range(int(input()))]
