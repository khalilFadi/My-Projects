n = int(input())
f = [0 for i in range(10e6 + 1)]
x = list(map(int, input().split()))
for e in x:
    factor = []
    i = 2
    m = e
    while i * i <= e:
        cnt = 0
        while e % i == 0:
            cnt += 1
            m //= i
        if cnt != 0:
            factor.append((i, cnt))
        i += 1
    if m > 1:
        factor.append((m, 1))
    for p, a in factor:
        f[p] += a
d = 1
MOD = 10e9 + 7
for a in f:
    d = d * (a + 1) % MOD
print(d)