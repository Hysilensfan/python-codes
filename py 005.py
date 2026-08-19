s: int = int(input())
D_conver: int = 24*60**2
H_conver: int = 60 ** 2
M_conver: int = 60
print(f"{s // D_conver}D{s % D_conver // H_conver}H{s % (D_conver) % (H_conver)// M_conver}M{s % (D_conver) % (H_conver) % M_conver}S")
"""
1day = 24hours
1hour = 60minutes
1minute = 60seconds
1day = 24hour x 60minute x 60second = 86400seconds
"""
