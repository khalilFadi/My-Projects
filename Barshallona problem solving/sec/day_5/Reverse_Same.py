n = int(input())
val = raw_input()
result = not  (len(val) % 2)
def check(string):
    my_list = []

    for i in range(len(string)):
        if string[i] in my_list:
            my_list.remove(string[i])
        else:
            my_list.append(string[i])
    
    if (len(my_list) == 0 and len(string) % 2 == 0) or (len(my_list) == 1 and len(string) % 2 != 0):
        return 1
    else:
        return 0
    
print("YES" if check(val) else "NO")
