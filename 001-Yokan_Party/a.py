N, L = [int(x) for x in input().split()]

K = int(input())

A = [int(x) for x in input().split()]

def binary_search():
    """めぐる式二部探索

    Returns:
        isOK を満たす最小/最大のL
    """
    ok = -1 
    ng = L + 1

    while(abs(ok-ng)>1):
        mid = int((ok+ng)/2)
        if isOK(mid):
            ok = mid
        else:
            ng = mid

    return ok

def isOK(mid):
    """
    長さ mid 以上で K 個以上に分割できるか調べる

    Args:
        mid (int): 長さ mid

    Returns:
        bool: [description]
    """
    start = 0
    end = 0
    cut_cnt = 0
    for a in A:
        end = a
        if end - start >= mid:
            start = a
            end = a
            cut_cnt += 1
            if cut_cnt == K:
                break
    if L - start >= mid and cut_cnt == K:
        return True
    else:
        return False

print(binary_search())
