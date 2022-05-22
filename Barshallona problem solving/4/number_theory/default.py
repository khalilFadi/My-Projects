def is_prime(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

def divisiors(n):
    ans = []
    i = 1
    while i * i <= n:
        if n % i == 0:
            ans.append(i)
            if i * i != n:
                ans.append(n // i)
        i += 1
    return ans

#gratest common divisor
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

#least common multiple 
def lcm(a, b):
    return a * b // gcd(a, b)


#check for intersection
list1 = []
list2 = []
list(set(list1).intersection(list2))

print(lcm(3, 5))