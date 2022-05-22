n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    output = 0
    for i in range(1, b):
        print(i ** 3)
        if a <= (i ** 3) <= b:
            output += 1
        else:
            break
        break
    print(output)