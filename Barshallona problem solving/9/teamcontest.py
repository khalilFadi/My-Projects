import sys
import threading

sys.setrecursionlimit(10**9)
threading.stack_size(2**26)

visited = [0] * 200005
g = []
def dfs(v):
    visited[v] = 1
    for u in g[v]:
        if visited[u] == 0:
            dfs(u)
def main():
    n, m, start, goal = map(int, input().split())
    for _ in range(n):
        g.append([])

    for i in range(m):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        g[a].append(b)
        g[b].append(a)    

    dfs(start - 1)
    if len(visited) == len(g):
        print("YES")
    else:
        print("NO")

threading.Thread(target=main).start()