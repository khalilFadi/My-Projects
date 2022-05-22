num = int(input()) 
maxn = num
fib = [[0, 0, 0] for i in range(maxn + 1)]
fib[1][0] = 2
fib[2][0] = 2
fib[2][1] = 1
fib[2][2] = 1
for i in range(3, maxn + 1):
    fib[i][0] = fib[i - 1][0] + fib[i - 1][1] + fib[i - 1][2]
 
    fib[i][1] =  fib[i - 1][0]
    fib[i][2] = fib[i - 1][1]   
    if i > 4:
        fib[i - 3] = None


num = num % int(1e9+7)
print(int(fib[num][0] + fib[num][1] + fib[num][2])% int(1e9+7))    