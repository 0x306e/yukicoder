def prime_decomposition(N):
    M = N
    i = 2
    table =[]
    while i * i <= N:
        while M % i == 0:
            M /= i
            table.append(int(i))
        i += 1
    if M > 1:
        table.append(int(M))
    return table


if __name__ == '__main__':
    N = int(input())
    li = prime_decomposition(N)
    if len(li) <= 2:
        print('NO')
    else:
        print('YES')
