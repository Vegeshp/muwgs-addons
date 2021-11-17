from muwgs import english_dict
from copy import copy
from collections import deque


def crosswords(s: str):
    '''
    given format string of alphabets and '*', return all possible words
    :param s: str, input string
    '''
    s = list(s)
    queue = deque()
    queue.append(s)
    while True:
        left = queue[0]
        try:
            index = left.index('*')
        except:
            break
        queue.popleft()
        for i in range(ord('a'), ord('z') + 1):
            temp = copy(left)
            temp[index] = chr(i)
            queue.append(temp)
    return [x for x in [''.join(x) for x in queue] if english_dict.check(x)]
