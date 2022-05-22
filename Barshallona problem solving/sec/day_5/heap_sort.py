def heap_sort(i, vec):
    if i < 0:
        return vec
    head = i
    left = (i * 2) + 1
    right = (i * 2) + 2
    size = len(vec)
    k = int((i - 1) / 2)
    if left < size and vec[left] < vec[head]:
        vec[left], vec[head] = vec[head], vec[left]
        vec = heap_sort(int((i - 1) / 2), vec)
    if right < size and vec[right] < vec[head]:
        vec[right], vec[head] = vec[head], vec[right]
        vec = heap_sort(int(((i - 2) / 2)), vec)
    return vec

def extractor(vec):

    for i in range(num):
        vec = heap_sort(i, vec)
    for i in range(num):
        vec = heap_sort(i, vec)
    for i in range(num):
        print(vec[0], end = " ")
        vec.pop(0)
        vec = heap_sort(0, vec)

num = int(input())
if num != 0:
    vec = list(map(int, input().split()))
    extractor(vec)