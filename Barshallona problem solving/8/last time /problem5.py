n = int(input())

result = 0
dif = [0 for i in range(n + 1)]
dif[3] = 1
dif[4] = 2
for i in range(3, n + 1):
    dif[i] = dif[i - 1] + dif[i - 2]
print(dif[n] % (1e9 + 7))