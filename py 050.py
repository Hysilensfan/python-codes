# First method
a, b = [list(map(int, input().split())) for _ in range(2]
print(a[0] * b[0] + a[1] * b[1] + a[2] * b[2])

# Second method
print(sum(a * b for a, b in zip(*[map(int, input().split()) for _ in range(2)])))
