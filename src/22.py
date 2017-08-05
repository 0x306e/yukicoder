def correspond(N: int, STR: str):
    S = STR[N-1:N]
    i = N
    l = 1
    if S == '(':
        while l != 0:
            if STR[i:i+1] == '(':
                l += 1
            else:
                l -= 1
            i += 1
    else:
        while l != 0:
            if STR[i-2:i-1] == ')':
                l += 1
            else:
                l -= 1
            i -= 1
    return i


if __name__ == '__main__':
    N = list(map(int, input().split()))
    STR = input()
    print(correspond(N[1], STR))
