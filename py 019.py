#first compose method
for _ in range(9):
    n=  input();tT = tL = 0 #default total value is 0
    if n == "Tiger":
        tT += 1
    else:
        tL += 1
print("Tiger" if tT > tL else "Lion")
#second compose method
print("Tiger" if sum(input()=="Tiger" for _ in range(9)) > 4 else "Lion") #logic clearly version,just judges the "Tiger"'s appeared dights greater than the "Lion"'s appeared dights
