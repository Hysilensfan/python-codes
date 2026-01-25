def happy(s):
    n = set()
    while s != 1:
        if s in n:
            break
        n.add(s);t=0
        for e in range(len(str(s))):
            t += int(str(s)[e])**2
        s = t
    else:
        return True
    return False
for i in range(int(input())):
    s = int(input())
    print("T" if happy(s)else"F")
