#number theory 
""" Divisble signs 2, 3, 9, 7, 11, 13
    Find the module (take the remainder) #Long % small
    Gratest common Divisor of 2 numbers or more 
"""
#Divisibility signs:
""" 257855102344
    check if this number is divisible by 2 or 5
        We can check the last number if its divisble by 2 or 5
"""
""" the idea is to:
    1) get the sum of digits 
    2) check if its divisble by 
"""


#GCD (Gratest Common Divisors):
""" 
12 1, 2, 3, 4, 6, 12
19 1, 19 
"""
""" 
a, b | a:b   ":" -> is divisble 
d    | d:b   "b" -> common divisors

64: 1, 2, 4, 8, 16, 32, 64
42: 1, 2, 3, 6, 7, 14, 21, 42
    GCD(64, 42) --> 2

60: 1, 2, 3, 6 ... 
42: 1, 2, 3, 6 ...
    GCD(60, 42) --> 6
"""
# 1 <= a, b <= 10e9
a = 60
b = 42
gcd = 1
while a!=0 and b != 0:
    if a > b:
        a = a % b
    else:
        b = b % a
gcd = a + b
""" 
Prperties:
0) GCD(0,x) = X
1) GCD(a, b) = GCD(a, b -a)
2) GCD(a, b) = GCD(a, b % a)
"""

print(gcd)





# for a list
def gcd(a, b):
    while a != 0 and b != 0:
        if a >b :
            a = a % b
        else:
            b = b %  a
    gcd = a + b 
    return gcd
a = #the list
ans = gcd(a[0], a[1])
for i in range(2, n):
    ans = gcd(ans, a[i])
print(ans)


#numeral system 
""" 
10 bottles --> 000-1010(how the computer reads it)
X  bottles (latin)

34679 = 9 + 7*10 + 6*100 + ...
10011 ==> 1*1 + 0*2 + 0*4 + 1*8 + 1*16 --> 25
the idea is:
1) 9 % 2 == 1
    9 / 2 = 4
   4 % 2 == 0
    4 / 2 = 2
    ....
continue then take the 1 and 0 from the bot and go
 to the top 
"""
n = int(input())
binary_representation = ""
while n > 0:
    #change the 2 to the number needed 
    binary_representation += str(n % 2)
    n = n // 2

print(binary_representation[::-1]) 

#change from base 7 to any base
base_7 = input()
ans = 0

base_7 = base_7[::-1]
x= 1
for c in base_7:
    ans += int(c) * x
    x *= 7
print(ans)


#recursion basic case
def f(b):
    if b == 1:
        return 1
    a = f(b - 1)
    return b
#version 2
calculated = {}
MOD = 1000000007
def f(n):
    if n in calculated:
        return calculated[n]
    
    if n <= 2:
        return 1
    l = f(n - 1)
    r = f(n - 2)
    calculated[n] = (l + r) % MOD
    return (l + r)%MOD

n = int(input())
print(f(n))
print(calculated)


#problem B from Problem 10-Apr
n = int(input())
calculated = {}
module = 1000000007 
def f(n):
    if n <= 2:
        return 1
    if n in calculated:
        return calculated[n]
    elif n % 2 == 0:
        calculated[n] = (f(9 * n // 11) + f(3 * n // 5)) % module
    else:
        calculated[n] = (f(n - 3) + f(n - 7)) % module
    return calculated[n]
print(f(n))
