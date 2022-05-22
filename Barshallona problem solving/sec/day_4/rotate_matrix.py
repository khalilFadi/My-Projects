def rotate_clockwise(vec):
    result = []
    version1 = []
    for x in range(len(vec)):
        for i in range(len(vec)):
            version1.insert(0,vec[i][x])
        version2 = version1
        result.append(version2)
        version1 = []
    return result
def rotate_not_clockwise(vec):
    result = []
    version1 = []
    for x in range(len(vec) - 1, -1, -1):
        for i in range(len(vec) - 1, -1, -1):
            version1.insert(0,vec[i][x])
        version2 = version1
        result.append(version2)
        version1 = []
    return result
n, q = map(int, input().split())
vec = []
for i in range(n):
    vecs = list(map(int, input().split()))
    vec.append(vecs)
nums = list(map(int, input().split()))
k = 0
while q > 0:
    if nums[k] == 1:
        vec = rotate_clockwise(vec)
        k += 1
        q -= 1
    else:
        vec = rotate_not_clockwise(vec)
        k += 1
        q -= 1
for i in vec:
    print(*i)