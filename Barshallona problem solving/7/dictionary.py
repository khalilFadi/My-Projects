#dynamic programming 
""" 
 * Divide and Conquer
    * divide the problem into sub problems
 * top-down and bot-up

"""
#Bot-up algorathim
def factorial(n):
    fact = [0 for i in range(n + 1)]
    fact[0] = 1 #base caes
    for i in range(1, n + 1):
        fact[i] = fact[i - 1] * i
    return fact[n]

#top-down algorathim
def fact(n):#recursive function
    if n == 0:
        return 1
    return n * fact(n - 1)
#compute the factorial from 1 to 100 q times
q = int(input())
for quer in range(q):
    b = int(input())
    print(fact(b))
     
#save the elements already used
# this reuse all the functions and some variables used above into a more effective form 
#this use the top down approch of memorization at which the data is saved in the fact array
maxn = 10000
fact = [None for i in range(maxn + 1)]
fact[0] = 1
def factorial2(n):
    if fact[n]:
        return fact[n]
    if n ==0:
        return 1
    fact[n]  = n * factorial2(n - 1)
    return fact[n]

fact = [0 for i in range(maxn + 1)]
fact[0] = 1
for i in range(1, maxn + 1):
    fact[i] = fact[i - 1] * i
q = int(input())
for query in range(q):
    n = int(input())
    print(fact[n])

#fibonacci 
#fib[0] = fib[1] = 1
#fin[n] = fib[n -1] + fin[n - 2]

maxn = 100
fib = [0 for i in range(maxn)]
fib[0] = 1
fib[1] = 1
for i in range(2, maxn):
    fib[i] = fib[i- 1] + fib[i -  2]
q = int(input())
for query in range(q):
    num = int(input())
    print(fib[num])