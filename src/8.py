def judge(N, K):
    if N <= K+1:
        return True
    tmp = K + 1
    k = 1
    while K * k <= N:
        if N - 1 == tmp * k:
            return False
        k += 1
    return True


if __name__ == '__main__':
    P = int(input())
    for i in range(P):
        N = list(map(int, input().split()))
        if judge(N[0], N[1]):
            print("Win")
        else:
            print("Lose")