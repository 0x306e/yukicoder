if __name__ == '__main__':
    L = int(input())
    M = int(input())
    N = int(input())

    SUM = L*100 + M*25 + N
    Hnd = (SUM % 1000) // 100
    TwF = (SUM % 100) // 25
    One = (SUM % 25)

    print(Hnd + TwF + One)