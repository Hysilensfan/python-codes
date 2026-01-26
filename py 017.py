for _ in range(int(input())):
    s = int(input());t = True
    if s < 2:
        t = False
    else:
        for i in range(2, int(s**0.5)+1): #using the square root for save calculation times,because this problem descripition that can only  be calculated in 1 second
            if s % i == 0:
                t = False
                break
    print("Y"if t else"N")
