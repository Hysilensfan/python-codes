from itertools import combinations as c
from collections import Counter as Ct

hand_type: dict = {
    (1, 4): 6,  # Four of a Kind A pairs and Sanjo
    (2, 3): 5,  # Gourd , composed of one pair and sanjo
    (1, 1, 3): 3,  # Sanjo
    (1, 2, 2): 2,  # Two pairs, but 「NOT THE Four of a Kind」
    (1, 1, 1, 2): 1,  # A pairs
}


def suit_judge(d: int) -> str:  # suit convert
    if 14 > d > 0:
        return "spades"
    elif 27 > d > 13:
        return "hearts"
    elif 40 > d > 26:
        return "diamonds"
    elif 53 > d > 39:
        return "clubs"
    else:
        return ""


def thepoker_highestscore(processes: c) -> int:
    directory: list = []
    for tuples in processes:
        ranks: list = [(x - 1) % 13 + 1 for x in tuples]
        cnt: dict = Ct(ranks)
        freq: tuple = tuple(sorted(cnt.values()))
        flush: bool = len(set(suit_judge(x) for x in tuples)) == 1  # Using the Equality to get the boolean
        nums: list = sorted(ranks)
        straight: bool = (
                nums == list(range(nums[0], nums[0] + 5))
                or nums == [1, 10, 11, 12, 13]
        )  # Identification of special cases
        if straight and flush:
            score = 7
        elif straight:
            score = 4
        else:
            score = hand_type.get(freq, 0)  # If it's None pair return 0
        directory.append(score)
    return max(directory)


[print(thepoker_highestscore(c(list(map(int, input().split())), 5))) for i in
 range(int(input()))]  # Stochastic draw 5 cards from 6 cards
