#first method
for _ in range(int(input())):
    s: int = list(input())
    t: int = 0
    for c in s:
        t += int(c) # To logging every numbers of digits's sum
    print(t)
#second method
[print(sum(map(int, input()))) for _ in range(int(input()))]
