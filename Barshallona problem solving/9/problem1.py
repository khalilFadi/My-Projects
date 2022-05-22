n, m = map(int, input().split())
visited = [0] * 200005
ver = []
for _ in range(n):
        ver.append([])

def dfs(v):
    visited[v] = 1
    for u in ver[v]:
        if visited[u] == 0:
            dfs(u)

for i in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    ver[a].append(b)
    ver[b].append(a)

dfs(0)
num = visited.index(0)
if n == num:
    print("YES")
else: 
    print("NO")