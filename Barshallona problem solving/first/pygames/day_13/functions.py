import random 
def find_smallest_list_num(lis):
    minumm = lis[0]
    position = 0
    for i in lis:
        if lis[i] < minumm:
            minumm = lis[i]
            position = i
    return minumm
def find_smallest_list_pos(lis):
    minumm = lis[0]
    position = 0
    for i in lis:
        if lis[i] < minumm:
            minumm = lis[i]
            position = i
    return position
def find_maximum_list_num(lis):
    minumm = lis[0]
    position = 0
    for i in lis:
        if lis[i] > minumm:
            minumm = lis[i]
            position = i
    return minumm
def find_maximum_list_pos(lis):
    minumm = lis[0]
    position = 0
    for i in lis:
        if lis[i] > minumm:
            minumm = lis[i]
            position = i
    return position
def sum_list(lis):
    result = 0
    for i in lis:
        result += lis[i]
    return result
def random_list(lis):
    n = random.randint(0,len(lis) - 1)
    return lis[n]
def odds_list(liss):
    var = liss
    output = []
    for i in range(len(var)):
        if var[i] % 2 == 0:
            output.append(var[i])
    return output
def list_of_word(words, n):
    for i in words:
        if len(i) > n:
            print(i)
def remove_all_duplicates(lis):
    output = []
    for i in range(len(lis)):
        transform = True
        for x in range(i, len(lis)):
            if i != x and lis[i] == lis[x]:
                transform = False
        if transform == True:
            output.append(lis[i])
    return output
 
var = [1, 2, 3, 4]
var = odds_list(var)
for i in var:
    print(i)