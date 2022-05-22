maxn = 60000
fib = [[0, 0, 0] for i in range(maxn + 1)]
fib[1][0] = 2
fib[2][0] = 2
fib[2][1] = 1
fib[2][2] = 1
for i in range(3, maxn + 1):
    fib[i][0] = fib[i - 1][0] + fib[i - 1][1] + fib[i - 1][2]
 
    fib[i][1] =  fib[i - 1][0]
    fib[i][2] = fib[i - 1][1]   

num = int(input()) 
print(fib[num][0] + fib[num][1] + fib[num][2])    