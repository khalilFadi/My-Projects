import random

def partition(a, low, high):
    r = -1
    a[r], a[high] = a[high], a[r]
    pivot = a[high]
    i = low
    j = high - 1
    while True:
        while i <= j and a[i] < pivot:
            i+= 1
        while i <= j and a[i] > pivot:
            j -= 1
        if a[i] > a[j]:
            a[i], a[j] = a[j], a[i]
        else:
            break
    a[high], a[j] = a[high], a[j]
    return j
def quick_sort(a, low, high):
    if low < high:
        p  = partition(a, low, high)
        quick_sort(a, low, p - 1)
        quick_sort(a, p + 1, high)

n = int(input())
vec = list(map(int, input().split()))
quick_sort(vec, 0, len(vec) -1)
print(vec)