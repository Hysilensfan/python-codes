for i in range(int(input())):
    a,b = input().split()
    for e in a:
        c = (ord(e) - ord('A')+int(b))%26+ord('A')
        print(chr(c), end="")
    print()
