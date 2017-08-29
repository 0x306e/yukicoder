import copy


def bfs(N):
    queue = [1]
    visited = []
    cnt = 0
    while queue:
        label = copy.deepcopy(queue)
        queue.clear()
        cnt += 1
        while label:
            pl = label.pop(0)
            if pl == N:
                return cnt
            if pl < 1 or N + 1 < pl:
                continue
            if pl in visited:
                continue
            visited += [pl]
            tmp = int(str(bin(pl)).count('1'))
            queue += [pl+tmp, pl-tmp]
    return -1


if __name__ == '__main__':
    N = int(input())
    print(bfs(N))
