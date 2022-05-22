sumofnum = 0
num1 = int(input())
for i in range(1, num1 + 1):
    if num1 % i == 0:
        sumofnum += 1
print(sumofnum)