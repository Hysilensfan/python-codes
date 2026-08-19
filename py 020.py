#first method
for _ in range(int(input())):
    s: str = list(input())
    v: int = int(s[0])
    for i in range(1, len(s)):
        if i % 2 != 0:
            v += int(s[i])
        else:
            v -= int(s[i])
    print(v)

#second method
for i in range(int(input())):
    e, digit = input(),2
    tot, e = int(e[0]), e[1:]
    for k in e:
        tot = tot + int(k) if digit % 2 == 0 else tot - int(k)
        digit += 1
    print(tot)

#third method
for _ in range(int(input())):
    s: str = input()
    v: str = int(s[0])
    v += sum(map(lambda i: int(s[i]) if i % 2 != 0 else -int(s[i]), range(1, len(s))))
    print(v) 
