num = input("input your lucky number")
if num == 0:
    print("zero")
elif num < 1 and num > 0:
    print("small")
elif num >= 1000000000:
    print("large")
elif num < 0:
    print("negative")
elif num > 0:
    print("positive")