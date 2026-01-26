#first compose method
a , b = [int(c) for c in input().split()];print((b - a + 200)%200) # this is an explanation of list comprehension's => a,b are our inputs which imported into c, then, turn c into integer(using the int function) so we can short for a list comprehension:"a , b = [int(c) for c in input().split()])"
#second compose method
a , b = input().split();print((int(b) - int(a) + 200)%200) # same with above this second paragraph 's list comprehension,but this code is more convenient for read and understand
