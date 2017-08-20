def twice_decomposition(N):
    if N in [1, 2, 3]:
        return []
    i = 2
    cnt = 0
    lst = []
    while i * i <= N:
        while N % i == 0:
            if cnt >= 2:
                lst.append(N)
                return lst
            N /= i
            lst.append(i)
            cnt += 1
        i += 1
    return lst


if __name__ == '__main__':
    N = int(input())
    ls = twice_decomposition(N)
    try:
        if ls[0] * ls[1] == N:
            print('NO')
        else:
            print('YES')
    except IndexError:
        print('NO')
