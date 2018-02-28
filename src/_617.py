if __name__ == '__main__':
    N, K = input().split()
    N, K = int(N), int(K)
    A = [int(input()) for i in range(N)]
    A.sort(reverse=True)
    tmp = K
    for i in A:
        if i <= tmp:
            tmp -= i
    print(K-tmp)