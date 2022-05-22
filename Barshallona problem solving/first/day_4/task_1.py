var = int(input())
string = input()
start = 0
end = var
for i in range(var):
    if string[i] == 'x':
        start = i
        break
for i in range(var - 1, 0, -1):
    if string[i] == 'x':
        end = i
        break
for i in range(start + 1):
    print(string[i], end = "")
for i in range(end, var):
    print(string[i], end = "")