y: int = int(input())
ans: str = "a normal year"
if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
    ans: str = "a leap year"
print(ans)
