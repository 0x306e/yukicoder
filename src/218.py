import math

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    c = int(input())
    nm = math.ceil(a / b)
    sp = math.ceil(a / c)
    if sp <= nm * 2 / 3:
        print('YES')
    else:
        print('NO')
