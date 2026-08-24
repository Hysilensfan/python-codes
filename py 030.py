# First method
for i in range(int(input())):
    n: str = input()
    while True:
        if n != n[::-1]:
            n: str = str(int(n) + int(n[::-1]))
        else:
            print(n)
            break

# Second method
echo = lambda s: s if str(s) == str(s)[::-1] else echo(s + int(str(s)[::-1]))

[print(echo(int(input()))) for _ in range(int(input()))]

