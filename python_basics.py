def my_function(x, y):
    print(x,"",y)

print(my_function("John", "Doe"))

def cube(x):
    return x*x*x

print(cube(2))

def power(num, x=1):
    result = 1
    for i in range(x):
        result = result * num
    return result

print(power(10))
print(power(10, x=2))
print(power(num=10, x=3))
print(power(x=4, num=10))

def running_total(*args):
    result = 0
    for x in args:
        result = result + x
    return result

print(running_total(1, 2, 3, 4, 40))

def main():
    print("Hello, world")

if __name__== "__main__":
    main()

