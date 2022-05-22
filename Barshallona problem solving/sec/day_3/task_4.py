num = int(input())
if num > 0:
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
def are_equal(i):
    if (a[i] > a[i - 1]) and (b[i] > b[i - 1]):
        return True
    elif (a[i] < a[i - 1]) and (b[i] < b[i - 1]):
        return True
    else:
        return False
Result = True
m = 0
for i in range(1, num):
    m = i
    if are_equal(i) != True:
        Result = False
        break
ver = "Bob" if num == 1 else "Alice" if Result else ("Bob \n" + str(a[m - 1])+ " " + str(a[m]))
print(ver)
