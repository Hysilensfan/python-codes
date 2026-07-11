# first method
from ast import literal_eval as a
print((str(list(map(list,zip(*(a(input())[::-1])))))).replace(" ",""))
# second method
from ast import literal_eval as l
print(str([*[list(a) for a in zip(*reversed(l(input())))]]).replace(" ", ""))
