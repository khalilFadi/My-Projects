k = int(input())
vares = [[]]
vares.append([])
for i in range(k):
    k, n = map(int, input().split())
    vares[0].append(n)
    vares[1].append(k)

def check_swap(i):
    if i + 1 == len(vares[1]):
        return 0
    if vares[1][i] <= vares[1][i + 1]:
        vares[1][i], vares[1][i + 1] = vares[1][i + 1], vares[1][i]
        vares[0][i], vares[0][i + 1] = vares[0][i + 1], vares[0][i]
    return check_swap(i + 1)
for i in range(len(vares[1])):
    check_swap(0)
for i in range(len(vares[1])):
    print(vares[1][i], end = " ")
    print(vares[0][i])