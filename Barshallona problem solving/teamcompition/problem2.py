n = int(input())
s = input()
result = n
length = 2
for i in range(len(s) - length):
    if s[i] == s[i + length]:
        result += 1
print(result)       