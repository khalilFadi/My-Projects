def function(x, y):
    return (2 * x) * y


largest = 0
lar_x = 0
lar_y = 0
for x in range(500):
    for y in range(500):
        if (2 * x) + y == 500:
            largest = function(x, y)
            lar_x = x
            lar_y = y
print(lar_x, lar_y)