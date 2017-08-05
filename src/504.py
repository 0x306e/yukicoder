if __name__ == '__main__':
    N = int(input())
    K = int(input())
    rank = 1
    print(rank)
    for i in range(1, N):
        tmp = int(input())
        if tmp > K:
            rank += 1
        print(rank)
