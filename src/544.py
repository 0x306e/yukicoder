if __name__ == '__main__':
    STR = input()
    Idx = []
    index = -1
    while True:
        Idx.append(STR.find('7', index + 1))
        index = STR.find('7', index + 1)
        if Idx.__contains__(-1):
            break
    result = ""
    if len(Idx) >= 1:
        for i in range(Idx[0], len(STR)):
            if Idx.__contains__(i):
                result += '1'
            else:
                result += '0'
        org = int(STR) - int(result)
        print(org, result)
    else:
        print(-1)
