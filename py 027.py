for i in range(int(input())):
    s1,s2=input().split(",");g1,g2,tie = "1","2","0";r = g2
    if s1 == s2:
        r = tie
    elif (s1,s2) in [("O","Y"),("Y","P"),("P","O")]:
        r = g1
    print(r)
