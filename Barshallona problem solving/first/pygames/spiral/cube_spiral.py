def dayoftheweek(num):
    if num == 1:
        return "monday"
    elif num == 2:
        return "tuesday"
    elif num == 3:
        return "wednesday"
    elif num == 4:
        return "thursday"
    elif num == 5:
        return "friday"
    elif num == 6:
        return "saturday"
    elif num == 7:
        return "sunday"
inpu = int(input("what is the day: "))
print("tommorow will be ", dayoftheweek(inpu + 1))