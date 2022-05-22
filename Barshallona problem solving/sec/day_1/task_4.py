num = int(input())
vares = []
for i in range(num):
    var = list(map(int, input().split()))
    vares.append(var)

def check(searched):
    num = 0
    for i in searched:
        for x in vares:
            if i == x:
                num += 1
    if num == len(vares):
        return True
    else:
        return False

def search(x, y, stri, searching):
    if x > 1000 or y > 1000:
        return 0
    if check(searching):
        return searching
    ver = [x, y]
    searching.append(ver)
    return search(x + 1, y, stri + "R", searching), search(x, y + 1, stri + "U", searching)

thing = search(0,0,"", [])
if  thing != 0:
    print("YES")
    print(thing)
else:
    print("NO")