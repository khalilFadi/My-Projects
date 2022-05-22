num, k = map(int,input().split())
vec = []


def partition(arr, low, high):
    i = (low-1)         
    pivot = arr[high][2]     
 
    for j in range(low, high):
 
        if arr[j][2] <= pivot:
 
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)
 
 
 
def quickSort(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:
 
        pi = partition(arr, low, high)
 
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)



for i in range(num):
    vector = list(map(int, input().split()))
    vector.insert(0, vector[1]/vector[0])
    vec.append(vector)
# quickSort(vec, 0, len(vec) - 1)
vec.sort()

num = 0
for i in range(k):
    num += vec[i][2]
for i in range(k, len(vec)):
    num += vec[i][1]
print(num)
