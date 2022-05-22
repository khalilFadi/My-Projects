def delete_smallest(ver):
    print(ver[-1])
    ver.pop()

def organize(ver):
    ver.sort()
    ver.reverse()
    #i tried this but it took to much time and the time limit is 
    #being exeted so i dont know if this is allowed but i used it
        # x = 0
        # for i in range(len(ver)):
        #     if ver[x] < ver[i]:
        #         ver[x], ver[i] = ver[i], ver[x]
        #         x += 1
    return ver

n = int(input())
ver = []
for i in range(n):
    k = int(input())
    if k == -1:
        organize(ver)
        delete_smallest(ver)
    else:
        ver.insert(0, k)
