# sets; collection of zero or more immutable types
# sets do not allow duplicates and are unordered

my_set = {8, 2, 5, 'dog', True}
your_set = {100, 200, False, 'dog'}

print(len(my_set))
print("dog" in my_set)
print("\n")

print(my_set.union(your_set)) # returns a new set with all elements from both sets. Note: "dog" is not repeated
print(my_set | your_set) # another way to union two sets
print("\n")

print(my_set.intersection(your_set)) # retuns a new set with only items common to both sets
print(my_set & your_set) # another way to get intersection
print("\n")

print(my_set.difference(your_set)) # retuns all items in the first list not in the second, "dog" is gone
print(my_set - your_set) # another way to implement difference
print("\n")

print({"dog", True}.issubset(my_set)) # check whether all elements in one set are in the other
print({"dog", True} <= my_set) # another way to do subset operation
print({"dog", True, 500} <= my_set)

# methods
my_set.add("school") # adds element to the end of the set
print(my_set)
print("\n")

my_set.remove(5) # removes element from the set
print(my_set)
print("\n")

my_set.pop() # removes an arbitrary element frm the set
print(my_set)
print("\n")

my_set.clear() # removes all elements from set
print(my_set)
print("\n")


