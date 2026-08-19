for i in range(int(input())):
    s1, s2 = input().split(",")
    if s1 == s2:
        r = '0'
    elif (s1,s2) in [("O","Y"),("Y","P"),("P","O")]:
        r = '1'
    print(r)
