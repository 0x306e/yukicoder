import math


def _round(num):
    if (num % 1) < 0.5:
        return math.floor(num)
    else:
        return math.ceil(num)


if __name__ == '__main__':
    A, B = [int(i) for i in input().split()]
    ans = []
    for a in range(1, 102):
        for b in range(1, 102):
            tA = (100 * a) / (a + b)
            tB = (100 * b) / (a + b)
            rA = _round(tA)
            rB = _round(tB)
            if (_round((100 * a) / (a + b)) == A) and (_round((100 * b) / (a + b)) == B):
                ans.append(a + b)
    print(min(ans))
