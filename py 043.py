# First method
for _ in range(int(input())):
    x, y, m = map(int, input().split())
    print(x ** y % m)

# Second method
[print(pow(x, y, m)) for _ in range(int(input())) for x, y, m in [map(int, input().split())]]
