import math


def is_prime(n):
    if n == 0: return False
    if n == 1: return False
    if n == 2: return True
    for i in range(3, n, 2):
        if n % i == 0:
            return False
        if i > math.sqrt(n):
            break
    return True


if __name__ == '__main__':
    N = int(input())
    if is_prime(N):
        print(N + 1)
    else:
        print(N)
