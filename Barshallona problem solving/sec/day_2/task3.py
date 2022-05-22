num = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
result = True
if sorted(A) != sorted(B):
    result = False
value = "Yes" if result else "No"
print(value)
