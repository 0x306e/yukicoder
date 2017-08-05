def fizzBuzzString(N):
    cnt = N // 3 + N // 5
    return cnt * 2

if __name__ == '__main__':
    N = int(input())
    print(fizzBuzzString(N))