import itertools

from builtins import print


def chk(mx: int, lst) -> bool:
    if mx % 2 == 1:
        return False
    for i in W:
        comb = list(itertools.combinations(lst, i+1))
        print(comb)
        for j in comb:
            print(comb[j[0:1]])
            if mx//2 == mx - sum(comb[j]):
                return True
    return False


if __name__ == '__main__':
    N = int(input())
    STR = input().split()
    W = list(map(int, STR))
    SUM = sum(W)

    if chk(SUM, W):
        print("possible")
    else:
        print("impossible")
