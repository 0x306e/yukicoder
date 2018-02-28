def three(n):
    sam = 0
    while n > 0:
        sam += (n % 10)
        n //= 10
    if sam % 3 == 0:
        return True
    else:
        return False


def five(n):
    if n < 10:
        return False
    if (n // 10) == ((n % 100) // 10):
        return True
    else:
        return False


if __name__ == '__main__':
    N = int(input())
    t = three(N)
    f = five(N)
    if t and f:
        print('FizzBuzz')
    elif t:
        print('Fizz')
    elif f:
        print('Buzz')
    else:
        print(N)
