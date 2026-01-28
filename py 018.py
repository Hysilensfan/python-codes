#first compose method
for _ in range(int(input())):
    s = list(input());t= 0
    for i in range(len(s)):t += int(s[i]) # to logging every numbers of digits's sum
    print(t)
#second compose method
for _ in range(int(input())):s = input();print(sum(map(int,s)))
