
def splitString(str):
    arr = []
    stack = []
    flag = False
    for c in str:
        if c == "]":
            stack.append(c)
            arr.append("".join(stack))
            stack = []
            flag = False
            continue
        if flag:
            stack.append(c)
            continue
        if c == "[":
            stack.append(c)
            flag = True
            continue

        arr.append(c)
    return arr


str = "希望你happy[开心][开心]"
strArr = splitString(str)
print(strArr)
