from muwgs import english_dict, global_limit, global_x, global_y
from muwgs.utils.keyboard_utils import word_press
from collections import deque
import time


def wordament(s: str, press=True, print_result=False, n=4):
    '''solver for wordament
    :param press: bool, help to print
    :param print: bool, print to screen
    :param n(optional): int, default to 4
    '''
    def dfs(res, map, vis, current, i, j, n, limit):
        temp = ''.join(current)
        if len(temp) >= 3 and english_dict.check(temp):
            if not temp in res:
                res.add(temp)
                if print_result:
                    print(temp, flush=True)
                if press:
                    word_press(temp)
        if limit == 0:
            return
        for (dx, dy) in zip(global_x, global_y):
            tx, ty = i + dx, j + dy
            if tx < 0 or ty < 0 or tx >= n or ty >= n or vis[tx][ty] or map[tx][ty].endswith('-'):
                continue
            current.append(map[tx][ty][1:] if map[tx]
                           [ty].startswith('-') else map[tx][ty])
            vis[tx][ty] = True
            dfs(res, map, vis, current, tx, ty, n, limit - 1)
            vis[tx][ty] = False
            current.pop()
        return
    map = s.split()
    assert(len(map) == n * n)
    map = [map[i * n:(i + 1) * n] for i in range(n)]
    res, vis = set(), [[False for _ in range(n)] for _ in range(n)]
    current = deque()
    time.sleep(3)
    print('OK, ready to go', flush=True)
    for i in range(n):
        for j in range(n):
            if map[i][j].startswith('-'):
                continue
            for x in (map[i][j][:-1] if map[i][j].endswith('-') else map[i][j]).split('/'):
                current.append(x)
                vis[i][j] = True
                dfs(res, map, vis, current, i, j, n, global_limit)
                vis[i][j] = False
                current.pop()
    return res

__all__ = ['wordament']