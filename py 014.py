n = int(input())
for i in range(1,n+1): #controling number of column
    for u in range(1,i+1): #controling internal roop and print 1 to i
        print(u,end=' ') #print digits and add half space
    print() #newline
print() #newline
for i in range(1,n+1):
    for u in range(1,n-i+2): # #controling internal roop and print 1 to n-i+2
        print(u,end=' ')
    print()
print()
for i in range(1,n+1):
    for u in range(n,i-1,-1): # controling internal roop and print 1 to n-i+2,interval -1
        print(u,end=' ')
    print()
print()
for i in range(1,n+1):
    for j in range(n-i):
        print(' ',end=' ')
    for j in range(1,i+1):
        print(j,end=' ')
    print()
