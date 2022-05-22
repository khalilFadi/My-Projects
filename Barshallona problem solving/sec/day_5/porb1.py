n = int(input())
num = list(map(int, input().split()))

result = 0

for i in range(1, len(num)):
    if sum(num[0:i]) == sum(num[i:len(num)]):
        result += 1

print(result)