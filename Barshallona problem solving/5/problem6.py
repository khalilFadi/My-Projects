q = int(input())
for query in range(q):
    n = int(input())
    d = list(map(int, input()))
    d.sort()
    candidate = d[0] * d[-1]
    dc = []
    i = 2
    while i * i <= candidate:
        dc.append(i)
        if candidate % i == 0:
            dc.append(candidate // i)
        i += 1
    dc.sort()
    if dc == d:
        print(candidate)
    else:
        print(-1)