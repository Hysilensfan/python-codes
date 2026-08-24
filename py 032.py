# First method
for _ in range(int(input())):
    a: str = input()
    tot: int = 0
    if len(a) == 16:
        for i in range(len(a)):
            if i % 2 == 0:  # Even digit position
                d= int(a[i]) * 2
                if d > 9:
                    d -= 9
            else:
                d: int = int(a[i])
            tot += d
        if tot % 10 == 0:
            print('T')
        else:
            print('F')
    else:
        print('F')
# Second method
weight: tuple = (2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1)
credit_card = lambda s: 'T' if divmod(sum([sum(map(int, str(x))) * y for x, y in zip(s, weight)]), 10)[1] and len(
    s) == 16 else 'F'  # divmod() function will return tuple that include quotient and remainder from two parameters.

[print(credit_card(input())) for _ in range(int(input()))]
