num1 = int(input())
num1 -= 10
if num1 < 1:
    print(0)
elif num1 < 10 or num1 == 11:
    print(4)
elif num1 == 10:
    print(15)
else:
    print(0)
