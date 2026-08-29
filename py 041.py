for i in range(int(input())):
    c = input().split()
    tot = frame = i = 0
    while frame < 10:
        if i < len(c):
            if c[i] == "X":
                tot += 10
                if i + 1 < len(c):
                    if c[i + 1] == "X":
                        tot += 10
                    elif c[i + 1].isdigit():
                        tot += int(c[i + 1])
                if i + 2 < len(c):
                    if c[i + 2] == "X":
                        tot += 10
                    elif c[i + 2] == "/":
                        tot += 10 - int(c[i + 1])
                    elif c[i + 2].isdigit():
                        tot += int(c[i + 2])
                i += 1
            elif i + 1 < len(c) and c[i + 1] == "/":
                tot += 10
                if i + 2 < len(c):
                    if c[i + 2] == "X":
                        tot += 10
                    elif c[i + 2].isdigit():
                        tot += int(c[i + 2])
                i += 2
            elif c[i].isdigit() and i + 1 < len(c) and c[i + 1].isdigit():
                tot += int(c[i])
                if i + 1 < len(c) and c[i + 1].isdigit():
                    tot += int(c[i + 1])
                i += 2
            frame += 1
    print(tot)
