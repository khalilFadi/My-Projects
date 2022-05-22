import random 
def checkwinner(num1, num2):
    output = False
    if num1 > num2:
        if num1 == 3 and num2 == 1:
            output = True
        else:
            output = False
    elif num1 < num2:
        if num2 == 3 and num1 == 1:
            output = True
        else:
            output = False
    return output

g = input("play rock paper scissors: ")
computer = ["paper", "scissors", "rock"]
player = 0
if g == 'P':
    player = 1
elif g == 'S':
    player = 2
elif g == "R":
    player = 3
n = random.randint(0,2)
print("computer result: " ,computer[n])
if checkwinner(player, n):
    print(" yay u won")
else:
    print("looks like you are dump")
