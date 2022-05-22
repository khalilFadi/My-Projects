n = int(input())
vec = list(map(int, input().split()))
i = 0
while i < n - 1:
    if vec[i] < vec[i + 1]:
        vec[i] = vec[i + 1]
        i += 1
    i += 1
print(sum(vec))