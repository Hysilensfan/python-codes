ex = {
        1000:"M",900:"CM", 500:"D", 400:"CD",
        100:"C", 90:"XC", 50:"L", 40:"XL",
        10:"X", 9:"IX", 5:"V", 4:"IV", 1:"I"
    }

def int_to_roman(s: int) -> str:
    r: str = ""
    for i in ex.keys():
        while s >= i:
            s -= i
            r += ex[i]
    return r


[print(int_to_roman(int(input()))) for _ in range(int(input()))]
