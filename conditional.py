def cond_struct(x, y):
    if(x < y):
        st = "x is less than y"
    elif(x == y):
        st = "x is same as y"
    else:
        st = "x is greater than y"

    return st

print(cond_struct(10, 10))
print(cond_struct(100, 10))
print(cond_struct(10, 100))