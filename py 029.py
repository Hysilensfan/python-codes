from sys import stdin as c
for i in c:
    try:
        a, b = map(int, i.split())
        print(4 * a + 6 * b)
    except:
        pass
