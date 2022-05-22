k, n, m = map(int, input().split())
alice = list(map(int, input().split()))
bob = list(map(int, input().split()))
lists = alice + bob
result = True
lists.sort()
lists = list(dict.fromkeys(lists))
num = 0
numx = 0
for i in range(len(lists)):
    numx += i
for i in range(k):
    num += i
if numx != num:
    result = False
print("YES" if result else "NO")