s: int = int(input())
D_conver: int = 24*60**2
H_conver: int = 60 ** 2
M_conver: int = 60
print(f"{s // D_conver}D{s % D_conver // H_conver}H{s % (D_conver) % (H_conver)// M_conver}M{s % (D_conver) % (H_conver) % M_conver}S")
"""
1day = 24hour
1hour = 60minute
1minute = 60second
1day = 24hourx60minutex60second = 86400second
"""
