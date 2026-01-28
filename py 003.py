#first compose method
y=int(input())
ans="Wrong"
if y>2:
    ans=(y-2)*4+21
elif 0<y<=2:
    ans=y*10.5
print(ans)
