num = int(input())
var = list(map(int, input().split()))
output = "["
for i in range(num):
    output += str(abs(var[i]))
    if i != num - 1:
        output += ", "
output += "]"
print(output)  