# n m
# n1 n2 n3
# m1 m2
# result
# n1 <= m1 <= m2 <= n2 <= n3
c = int(input())
result = []
#x with n
def x_fun(num):
    return 2 * (num ** 2)
def y_fun(num):
    return (num ** 2) + (num * 100) + 1000
#y with m
x, y = 1, 1
result = []
# my_file = open("tabel.txt", "w")
while c > x + y - 2:
    output = x_fun(x) if x_fun(x) < y_fun(y) else y_fun(y) 
    # stri = str(x + y - 2) + " " + str(output) + "\n"
    # my_file.write(stri)
    result.append(output)
    f = x
    x += 1 if x_fun(x) <= y_fun(y) else 0
    y += 1 if not x_fun(x) < y_fun(y) and f == x else 0

#my_file.close()

print(result[c - 1])
