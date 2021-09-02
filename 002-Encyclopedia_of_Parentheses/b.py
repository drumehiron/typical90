# bit全探索での実装

N = int(input())

res = set()

def isOK(brackets):
    s = 0
    for b in brackets:
        if b == '(':
            s += 1
        else:
            s -= 1
        if s < 0:
            return False
    if s == 0:
        return True
    else:
        return False

for i in range(1<<N):
    brackets = ['('] * N
    for j in range(N):
        if((i >> j) & 1):
            brackets[N-1-j] = ')'
    if isOK(brackets):
        res.add(''.join(brackets))

for a in sorted(res):
    print(a)
