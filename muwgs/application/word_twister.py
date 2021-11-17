from muwgs import english_dict
from itertools import permutations


def word_twister(s: str, n: int):
    arr = []
    for x in permutations([s[i] for i in range(len(s))], n):
        arr.append(''.join([x[i] for i in range(n)]))
    arr = [x for x in list(set(arr)) if english_dict.check(x)]
    arr.sort()
    return arr
