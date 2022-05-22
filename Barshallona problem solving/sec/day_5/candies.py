import array
num = int(input())
var = list(map(int, input().split()))

ver = [[]]
for i in range(len(var)):
    if ver.index != 0:
        ver[ver.index(var[i])].append(i)
    else:
        ver.append((var[i], i))
print(ver)
