num = int(input())
ver = list(map(int, input().split()))
def search_for_alike(i):
    result = 0
    for x in range(i, len(ver)):
        if ver[x] == ver[i]:
            result += 1
    return result
output = []
Result = True
for i in range(len(ver)):
    if search_for_alike(i) == 2:
        output.append(ver[i])
    elif search_for_alike(i) > 2:
        Result = False

for x in output:
    for i in ver:
        if i == x: 
            ver.remove(i)
            break
ver.sort()
jk = "YES" if Result else "NO"
print(jk)
if Result:
    print(len(ver))
    print(*ver)
    print(len(output))
    print(*output)
