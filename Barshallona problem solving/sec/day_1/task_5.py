num = int(input())
var = list(map(int, input().split()))
result = 0
def search_for_alike(stri):
    global result
    numb = 0
    for i in range(len(var)):
        if var[i] == stri and var[i] != -1:
            var[i] = -1
            numb += 1
    if numb > 0:
        result += 1
for i in var:
    search_for_alike(i)
print(result)