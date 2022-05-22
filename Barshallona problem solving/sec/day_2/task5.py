n = int(input())
vers = []
for i in range(n):
    ver = list(map(int, input().split()))
    vers.append(ver)

def from_small_to_big(i):
    global vers
    if i <= 0:
        return 0
    if vers[i][1] <= vers[i - 1][1]:
        vers[i][1], vers[i - 1][1] = vers[i - 1][1], vers[i][1]
        vers[i][0], vers[i - 1][0] = vers[i - 1][0], vers[i][0]
        return from_small_to_big(i - 1)
def from_big_to_small(i):
    if vers[i][1] == vers[i + 1][1] and vers[i][0] < vers[i + 1][0]:
        vers[i][1], vers[i + 1][1] = vers[i + 1][1], vers[i][1]
        vers[i][0], vers[i + 1][0] = vers[i + 1][0], vers[i][0]
        return from_big_to_small(i + 1)
if n > 0:
    for i in range(1, n):
        from_small_to_big(i)
    for i in range(0, n - 1):
        from_big_to_small(i)
    for i in vers:
        print(*i)
else:
    print(0)
