n = 10e6
is_prime  = [True for i in range(n + 1)]
is_prime[0] = False
is_prime[1] = False
factor = [[] for i in range(n + 1)]
for i in range(2, n + 1):
    if is_prime[i]:
        factor[i].append((i, 1))
        for j in range(i * i, n + 1, i):
            is_prime[j] = False
            x = j
            cnt = 0
            while x % i == 0:
                cnt += 1
                x //= i
            factor[j].append((i, cnt))
q = int(input())
for query in range(q):
    x = int(input())
    print(len(factor[x]))
    for p, a in factor[x]:
        print(p, a)