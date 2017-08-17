if __name__ == '__main__':
    N = int(input())
    ans = 0  # answer
    seq = []  # temp list
    SUM = 0  # temp sum
    times = 0  # temp number of comb
    flag = False  # flag for remainder
    for i in range(N//2):
        for j in range(i):
            seq.append(2)
            SUM += 2
            times += 1
        while SUM < N:
            if N - SUM == 1:
                SUM += 1
            elif N - SUM == 2:
                SUM += 2
                flag = True
            else:
                seq.append(3)
                SUM += 3
                times += 1
        ans += pow(2, times) * 2 if flag else pow(2, times)
        seq.clear()
        SUM = 0
        times = 0
        flag = False
    print(ans)
