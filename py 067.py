roman = {
    'I': 1, 'V': 5,
    'X': 10, 'L': 50,
    'C': 100, 'D': 500,
    'M': 1000
}  # Basic roman characters.

def roman_to_int(s: str) -> int:
    tot = prev = 0
    for c in reversed(s):
        v = roman[c]
        if v < prev:
            tot -= v
        else:
            tot += v
        prev: int = v
    return tot


[print(roman_to_int(input())) for _ in range(int(input()))]
