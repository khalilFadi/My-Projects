def factorize(num):
    res = []
    p = 2
    n = num
    while n > 1 and p * p <= num:
        k = 0
        while n % p == 0:
            n/= p
            k += 1
        if k > 0:
            res.append((int(p), k))
        p += 1
    if n > 1:
        res.append((int(n), 1))
    return res  

def div_count(num):
    f = factorize(num)
    res = 1
    for _,  k in f:
        res *= (k + 1)
    return res

def sieve(num):
    is_prime = [True for i in range(num + 1)]
    is_prime[0] = False
    is_prime[1] = False
    primes = []
    for i in range(2, num + 1):
        if is_prime[i]:
            primes.append(i)
            for j in range(i* i, num + 1):
                is_prime[j] = False
    return primes

def sieve_and_factorize(num):
    is_prime = [True for i in range(num + 1)]
    is_prime[0] = False
    is_prime[1] = False
    primes = []
    f = [[] for i in range(num + 1)]
    for i in range(2, num + 1):
        if is_prime[i]:
            primes.append(i)
            for j in range(2* i, num + 1, i):
                is_prime[j] = False
                # checking the number of j??????
                n = j
                aplha = 0
                while n % i == 0:  
                    n //= i
                    aplha += 1
                f[j].append((i, aplha))

    return f
f = sieve_and_factorize(10)
for i in range(11):
    print(i, f[i])

def power(a, n):
    if n == 0:
        return 1
    return power(a *a, n // 2) * (a if n % 2 == 1 else 1)

print(sieve(12))