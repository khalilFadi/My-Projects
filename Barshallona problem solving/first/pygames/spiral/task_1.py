def checkgratestnum(num1, num2, num3):
    if num1 > num2:
        if num1 > num3:
            return num1
        if num3 > num1:
            return num3
    if num2 > num1:
        if num2 > num3:
            return num2
        if num3 > num2:
            return num3
num1 = input("Enter the first num: ")
num2 = input("secound num: ")
num3 = input("third num: ")
print("the biggest num is: ", checkgratestnum(num1, num2, num3))