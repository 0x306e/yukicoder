import math

if __name__ == '__main__':
    N = int(input())
    x = list(map(int, input().split()))
    SUM = max(x)
    x.remove(max(x))
    for i in range(N - 1):
        SUM += x[i] // 2
    print(SUM)
