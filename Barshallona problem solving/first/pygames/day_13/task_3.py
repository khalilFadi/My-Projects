def remove_all_duplicates(lis):
    for i in range(len(lis)):
        for x in range(len(lis)):
            if i != x and lis[i] == lis[x]:
                lis.remove(i)
    return lis
 