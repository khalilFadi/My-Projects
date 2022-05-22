
num = int(input())
nums = list(map(int, input().split()))

result = []
vers = []

for i in range(num):
    var = list(map(int, input().split()))
    vers += var
result = vers
vers.pop(0)
# while len(vers) != 0:
#     z = 0
    
#     result.insert(z, vers[0][0])
#     vers[0].pop(0)
#     if len(vers[0]) == 0:
#         vers.pop(0)

print(*result)