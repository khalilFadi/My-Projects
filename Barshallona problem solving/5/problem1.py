""" def sieve(num):
    is_prime = [True for i in range(num + 1)]
    is_prime[0] = False
    is_prime[1] = False
    primes = []
    for i in range(2, num + 1):
        if is_prime[i]:
            primes.append(i)
            for j in range(i * i, num + 1):
                if j % i == 0:
                    is_prime[j] = False
    return primes

num = int(input())
print(*sieve(num)) """

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
print(sieve_and_factorize(10))