from sys import stdin as c
for line in c:
    try:
        a, b = map(int, line.split())
        print(4 * a + 6 * b)
    except:
        pass
