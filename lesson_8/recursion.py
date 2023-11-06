def add_num(num):
    if(num >= 9):
        return
    total = num + 1
    print(total)

    return add_num(total)

add_num(5)