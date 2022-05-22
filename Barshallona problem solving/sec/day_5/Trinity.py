n = int(input())
num = list(map(int, input().split()))
def min_heapfiy(arr, i):
    l =  i * 2 + 1
    r = i * 2 + 2
    least = i
    if l < len(arr) and arr[least] > arr[l]:
        least = l
    if r < len(arr) and arr[least] > arr[r]:
        least = r
    if least != i:
        arr[i], arr[least] = arr[leas], arr[i]
        min_heapfiy(arr, least)

def build_heap(arr):
    for i in range(len(arr) - 1, -1, -1):
        min_heapfiy(arr, i)

build_heap(a)
print(*a)    
