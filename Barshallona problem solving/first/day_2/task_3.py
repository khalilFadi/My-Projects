
num1, num2, num3, num4 = map(int, input().split())
var = [num1, num2, num3, num4]
output = 0
for i in range(0,4):
    for x in range(i, 4):
        if i != x and var[i] == var[x]:
            output += 1
            break
        
print(output)