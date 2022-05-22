num = int(input())
vec = []


def partition(arr, low, high):
    i = (low-1)         
    pivot = arr[high][0]     
 
    for j in range(low, high):
 
        if arr[j][0] <= pivot:
 
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
    vector = [
        vector[0] * vector[0] +
        vector[1] * vector[1],
        vector[2]
    ]
    vec.append(vector)
# quickSort(vec, 0, len(vec) - 1)
vec.sort()

num = 0 
distance = 0
for i in vec:
    num += i[1]
    distance = i[0]
    if num >= 1000000:
        break
print(distance)