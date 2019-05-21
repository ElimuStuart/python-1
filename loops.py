# while loop
x = 0
while(x < 5):
    print(x)
    x = x + 1

# for loop
for i in range(3):
    print(i)

for i in range(3, 10, 2):
    print(i)

days = ["Mon", "Tue", "Wed", "Thur", "Fri", "Sat", "Sun"]
for day in days:
    print(day)

# continue and break statements
for i in range(6):
    if (i % 2 == 0):
        continue
    print(i)

for i in range(6):
    if (i == 2):
        break
    print(i)

# keep track on iterations using Enumerate()
days = ["Mon", "Tue", "Wed", "Thur", "Fri", "Sat", "Sun"]
for i, d in enumerate(days):
    print(i, d)