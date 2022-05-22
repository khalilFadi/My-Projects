a = int(input())
b = int(input())
result = 0
for i in range(a):
    for x in range(b):
        result += b ** a
print(result)