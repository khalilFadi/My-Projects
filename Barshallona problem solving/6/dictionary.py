def Fgcd(a, b):
    if b == 0:
        return a
    return Fgcd(b, a % b)


# gcd(a, b) = x * a + y * b
    # gcd(55, 80) = 55 * 3 + 80 * -2 = 5
#a, b => b, a % b, => .... =>, d, 0
#d = 1 * d = 0 8 0
    #x = 1 and y = 0
def egcdr(a, b):
    if b == 0:
        x = 1
        y = 1
        return a, x, y
    d, x1, y1 = egcdr(b, a % b)
    x = y1
    y = x1 - (a / b) * y1
    return d, x, y

def gcd(a, b):
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

print(egcdr(123, 12345))