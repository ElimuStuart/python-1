f = "abc"
def my_function():
    global f # global scope
    f = "xyz"
    return f

print(my_function())
print(f)

