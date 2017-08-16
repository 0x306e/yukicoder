if __name__ == '__main__':
    n = input()
    LEN = len(n)
    SUM = (LEN * 2) + 1
    for i in range(LEN):
        tmp = n[i:i+1]
        if tmp == '4':
            SUM += 1
        elif tmp == '6':
            SUM += 1
        elif tmp == '9':
            SUM += 1
        elif tmp == '0':
            SUM += 1
        elif n[i:i+1] == '8':
            SUM += 2
        else:
            pass
    print(SUM)
