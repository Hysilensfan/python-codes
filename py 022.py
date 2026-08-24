for i in range(int(input())):
    a, b = input().split()
    [print(chr((ord(e) - ord('A') + int(b)) % 26 + ord('A')), end="") for e in a]
    print()
