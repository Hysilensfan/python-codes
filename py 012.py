#first compose method
a , b = [int(c) for c in input().split()];print((b - a + 200)%200) # this is an explanation of list comprehension's => read our inputs(a,b) which stored to c, then, convert c into integer(using the int function) so we can using list comprehension:"a , b = [int(c) for c in input().split()])"
#second compose method
a , b = input().split();print((int(b) - int(a) + 200)%200) # same same result as above,but this code is more readable
