# First method
def operation(f: str) -> int:
    f: str = f.replace("-", "+-").split("+")
    k: int =  0
    for n in f:
        if n != "":
            k += int(n.strip())
    return k


for i in range(4):
    a, c = input().split("==")
    print("TRUE" if operation(a) == operation(c) else "FALSE")

# Second method
[print("TRUE" if eval(input()) else "FALSE") for _ in range(4)]
