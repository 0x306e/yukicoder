from builtins import print

global N
N = int(input())
location = 1
add = 1
cnt = 0
global list
list = []
visited = [False] * 10001


def dfs(L, add, cnt):
    if L > N+1 or L < 1 or visited[L]:
        return

    if L == N:
        list.append(cnt)
        return

    visited[L] = True
    L += add

    ad = int(str(bin(L)).count("1"))

    dfs(L, ad, cnt + 1)
    dfs(L, ad * -1, cnt + 1)

dfs(location, add, cnt + 1)
try :
    m = min(list) + 1
except ValueError :
    m = -1

print(m)
