#first compose method
for i in range(int(input())):
    s = input()
    if s==s[::-1]:
        print("Y")
    else:
        s=s.replace(" ","") # equal " s="".join(s.split(" ")) "
        print("Y"if s==s[::-1]else"N")
#second compose method
for i in range(int(input())):s = input().replace(" ","");print("Y" if s==s[::-1]else "N")
