#first method
a , b = [int(c) for c in input().split()]
print((b - a + 200) % 200) # this is an explanation of list comprehension's => read our inputs(a,b) which stored to c, then, convert c into integer(using the int function) so we can using list comprehension:"a , b = [int(c) for c in input().split()])"
#second method
a , b = map(int, input().split())
print(b - a + 200 if b - a < 0 else b - a)  # This version is easier to understand.
