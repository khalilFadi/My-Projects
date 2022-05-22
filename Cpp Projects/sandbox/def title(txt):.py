def title(txt):
    res = ""
    res += txt[0].upper()
    for i in range(1, len(txt) - 1):
        if txt[i] == ' ':
            res += txt[i + 1].upper()
        else:
            res += txt[i + 1]
    return res

print(title("khalil fadi hamad"))

