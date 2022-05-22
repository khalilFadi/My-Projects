n = int(input())
a = list(map(int, input().split()))

def merge_sort(l):
    if len(l) < 2:
        return l
    m = len(l) // 2
    left = l[:m]
    right = l[m:]
    left = merge_sort(left)
    right = merge_sort(right)

    i = 0
    j = 0
    result = []

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result
print(*merge_sort(a))