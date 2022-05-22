import math
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def agcd(a, b):
    x, y = 1, 0
    x1, y1 = 0, 1
    a1, b1 = a, b
    while b1 != 0:
        q = a1 // b1
        x, x1 = x1, x - q * x1
        y, y1 = y1, y - q * y1
        #x1 * a + y1 * b = b1
        a1, b1, = b1, a1 - q * b1
    #a1 = x * a + y * b
    return a1, x, y
def egcd(a, b):
    if b == 0:
        x = 1
        y = 1
        return a, x, y
    d, x1, y1 = egcd(b, a % b)
    x = y1
    y = x1 - (a / b) * y1
    return d, x, y
def Kgcd(a, b):
    while(b):
        a, b = b, a %b
    return a
a, b = map(int, input().split())
var = egcd(a, b)

print(a if a == b else 1)
#just tryng dont count this