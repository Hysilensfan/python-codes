# First method
def F(n: int) -> int:
    if n == 0:
        return 1
    tot = 0
    for left in range(n):
        right = n - 1 - left
        tot += F(left) * F(right)  # Recurtion
    return tot


def symmetric_bst(d: int) -> int:
    if d % 2 == 0:
        return 0
    return F((d - 1) // 2)


[print(symmetric_bst(int(input()))) for _ in range(int(input()))]
# Second method
def symmetric_bst(d: int) -> int:
    if d % 2 == 0:
        return 0
    recursive: list = [1]  # Minimum value is 1.
    for n in range(1, d + 1):
        tot: int = 0
        for left in range(n):
            right = n - 1 - left
            tot += recursive[left] * recursive[right]
        recursive.append(tot)
    return recursive[(d - 1) // 2]  # This position is used to find the mirrored left subtree.


[print(symmetric_bst(int(input()))) for _ in range(int(input()))]
