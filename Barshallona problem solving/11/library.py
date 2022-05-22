#organize n and m
# using the concecpt of going through each one at a time 
Anum, Bnum = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

def merge(a, b):
    ans = []
    i = 0
    j = 0
    while i < len(a) or j < len(b):
        if i == len(a):
            ans.append(b[j])
            j += 1

        elif j == len(b):
            ans.append(a[i])
            i += 1
        elif a[i] < b[j]:
            ans.append(a[i])
            i += 1
        else:
            ans.append(b[j])
            j += 1

    return ans
print(*merge(a, b))

#gets an array and sort it 
def sort(a):
    n = len(a)
    m = n // 2
    l = a[0 : m]
    r = a[m : n]
    # gets half and sorts it
    l = sort(l)
    # Merge 
    sorted_l = sort(l)
    sorted_r = sort(r)
    sorted_a = merge(sorted_l, sorted_r)
    return sorted_a

n = int(input())
a = list(map(int, input().split()))
print(*sort(a))

#Quick Sort
n = int(input())
a = list(map(int, input().split()))
def partition(l, r):
    pivot = a[(l + r) // 2]
    i = l - 1
    j = r + 1
    while True:
        i += 1
        j -= 1
        while a[i] < pivot:
            i += 1
        
        while a[j] > pivot:
            j -= 1
        
        if i >= j:
            return j
        a[i], a[j] = a[j], a[i]
    
def sort(l, r): 
    if l >= r:
        return 
    p = partition(l , r)
    sort(l, p)
    sort(p + 1, r)

sort(0, n - 1)
print(*a)

#City of lights
https://loc03.contest.codeforces.com/group/vT14M9h3TJ/contest/325715/problem/E
n = int(input())
arc = [1 for i in range(n + 1)]
num = int(input())
num_of_off = 0
mass = 0
def change_to_0(arc, n):
    global num_of_off, mass
    for i in range(1, len(arc)):
        if i % n != 0:
            continue

        if arc[i] == 1:
            arc[i] = 0
            num_of_off += 1
        else:
            arc[i] = 1
            num_of_off -= 1
    if num_of_off > mass:
        mass = num_of_off
    return arc
for i in range(num):
    z = int(input())
    arc = change_to_0(arc, z)
arc.pop(0)
x = 0
for i in arc:
    if i == 0:
        x += 1

print(mass)
#Secound try
n = int(input())
arc = [True for i in range(1, n + 1)]
num = int(input())
on = n
off = 0
maz = 0
    
while num >= 1:
    x = int(input())
    if x == 1:
        if arc[0] == True:
            off += 1
            on -= 1
        else:
            on += 1
            off -= 1
        arc[0] = not arc[0]
    for i in range(1, len(arc)):
        if (i + 1) % x == 0:
            if arc[i] == True:
                off += 1
                on -= 1
            else:
                on += 1
                off -= 1
            arc[i] = not arc[i]
    num -= 1
    maz = off if off > maz else maz


res = 0

print(maz)
#third try
n = int(input())
arc = [True for i in range(1, n + 1)]
num = int(input())
on = n
off = 0
maz = 0
    
while num >= 1:
    x = int(input())
    if x == 1:
        off, on = on, off
        arc = [not elem for elem in arc]
        maz = off if off > maz else maz
        num -= 1
        continue
    for i in range(x, len(arc) + 1, x):
        i -= 1
        if arc[i] == True:
            off += 1
            on -= 1
        else:
            on += 1
            off -= 1
        arc[i] = not arc[i]
        i += 1
    num -= 1
    maz = off - 1 if off > maz else maz

arc.pop(0)
res = 0

print(maz)
#one prob
n, m = map(int, input().split())
arc = list(map(int, input().split()))
arc.sort()
ma = arc[0]
for i in range(len(arc) - 1):
    if arc[i + 1] - arc[i] > ma:
        ma = arc[i + 1] - arc[i]

if m - arc[-1] > (ma / 2):
    ma = m - arc[-1]
    print(ma)
    exit()
elif arc[0] > (ma / 2):
    print(arc[0])
    exit()
print(ma / 2)