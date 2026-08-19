for i in range(int(input())):
    s = input().replace(" ","") # equal " s="".join(s.split(" ")) "
    print("Y" if s==s[::-1]else "N")
