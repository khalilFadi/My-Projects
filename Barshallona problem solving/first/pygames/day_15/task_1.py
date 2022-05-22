def find_last_and_first_num(var):
    result = [var[0], var[len(var) - 1]]
    return result

#example
example = [4,1,2,3,4,5,6,7,8,9,10]
var = find_last_and_first_num(example)
for i in range(len(var)):
    print(var[i])