#first compose method
for _ in range(int(input())):
    s = list(input())
    v = int(s[0])
    for i in range(1, len(s)):
        if i % 2 != 0:
            v += int(s[i])
        else:
            v -= int(s[i])
    print(v)
#second compose method
for _ in range(int(input())):
    s = list(input());v = int(s[0])
    for i in range(1, len(s)):w = lambda :i % 2 != 0;v += int(s[i]) if w() else - int(s[i])
    print(v)
#third compose method
for _ in range(int(input())):s = input();v = int(s[0]);v += sum(map(lambda i: int(s[i]) if i % 2 != 0 else -int(s[i]), range(1, len(s))));print(v)
