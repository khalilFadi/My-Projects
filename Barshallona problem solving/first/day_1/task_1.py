def check_prime(num):
    output = False
    if num > 1:
        for x in range(2, num//2 + 1):
            if num % x == 0:
                output = False
                break
            else:
                output =  True
    else:
        output = False
    return output

num1 = int(input())
for i in range(2, num1 // 2):
    if not check_prime(num1 - (i * 2)):
        print(i * 2)
        print(num1 - (i * 2))
        break
