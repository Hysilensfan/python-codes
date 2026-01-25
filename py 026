a = {
    'A': (1, 0), 'B': (1, 1), 'C': (1, 2), 'D': (1, 3), 'E': (1, 4),
    'F': (1, 5), 'G': (1, 6), 'H': (1, 7), 'I': (3, 4), 'J': (1, 8),
    'K': (1, 9), 'L': (2, 0), 'M': (2, 1), 'N': (2, 2), 'O': (3, 5),
    'P': (2, 3), 'Q': (2, 4), 'R': (2, 5), 'S': (2, 6), 'T': (2, 7),
    'U': (2, 8), 'V': (2, 9), 'W': (3, 2), 'X': (3, 0), 'Y': (3, 1),
    'Z': (3, 3)
}
t = [input().strip() for i in range(int(input()))]
def v(id):
    if len(id) != 10:
        return "F"
    if id[0] not in a:
        return "F"
    if id[1] not in '12':
        return "F"
    if not id[2:].isdigit():
        return "F"
    r = a[id[0]]
    n1, n2 = r
    i = [n1, n2] + [int(c) for c in id[1:]]
    w = [1, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1]
    t = sum(d * w for d, w in zip(i, w))
    return "T" if t % 10 == 0 else "F"
V = [v(tc) for tc in t]
print("\n".join(V))
