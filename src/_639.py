import math


def solve(n):
    if n == 0:
        return 1
    return solve(math.floor(n/3)) + solve(math.floor(n/5))


if __name__ == '__main__':
    N = int(input())
    print(solve(N))
