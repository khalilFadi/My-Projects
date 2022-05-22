num = int(input())
def Fgcd(a, b):
    if b == 0:
        return a
    return Fgcd(b, a % b)

one = num // 2
two = num // 2
if one + two != num:
    two += 1
gcd = Fgcd(one, two)
while one > 0:
    one -= 1
    two += 1
    if Fgcd(one, two) > gcd:
        gcd = Fgcd(one, two)
print(gcd)