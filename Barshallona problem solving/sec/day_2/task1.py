num = int(input())
ver = list(map(int, input().split()))
result = []

def search_position(n):
    position = 0
    for i in range(len(result)):
        if result[i] <= n:
            position = i + 1
    result.insert(position, n)
    return 0

for i in ver:
    search_position(i)
print(*result)
        
