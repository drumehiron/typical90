N = int(input())

if N % 2 != 0:
    import sys
    sys.exit()

N = int(N/2)

from functools import lru_cache

@lru_cache(maxsize=None)
def calc(N):
    res = set()
    if N == 1:
        res.add('()')
        return res
    else:
        for S in calc(N-1):
            res.add(f'({S})')
        for i in range(1,N):
            import itertools
            for S, T in itertools.product(calc(i),calc(N-i)):
                res.add(S+T)
        return res

res = calc(N)

for r in sorted(res):
    print(r)
