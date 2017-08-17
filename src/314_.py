import itertools


if __name__ == '__main__':
    N = int(input())
    ans = 0  # answer
    seq = []  # temp list
    SUM = 0  # temp sum
    times = 0  # temp number of comb
    for i in range(N//2):
        for j in range(i):
            seq.append(2)
            SUM += 2
            times += 1
        while SUM < N:
            if N - SUM == 1:
                SUM += 1
            else:
                seq.append(3)
                SUM += 3
                times += 1
        ans += len(list(itertools.combinations_with_replacement(seq, times)))
    print(ans)
