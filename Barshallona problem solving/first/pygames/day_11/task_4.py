#find the smallest num
num1 = input("enter the first num: ")
num2 = input("enter the secound num: ")
num3 = input("enter the third num: ")

def find_least_num(num1, num2, num3):
    if num1 < num2:
        if num1 < num3:
            return 1
        if num3 < num1:
            return 2
    elif num2 < num3:
        if num2 < num1:
            return 2
    else:
        return 3
print(find_least_num(num1, num2, num3))