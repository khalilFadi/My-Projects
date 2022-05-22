num = int(input())
ver = list(map(int, input().split()))
ver.sort()
least = abs(ver[0] - ver[1])
for i in range(1, len(ver) - 1):
    if abs(ver[i] - ver[i + 1]) < least:
        least = abs(ver[i] - ver[i + 1])
print(least)
