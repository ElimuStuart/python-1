# lists are ordered collections
# heterogeneous, meaning can hold any type of data

my_list = [1, 2, 3, True, 'hello'] 
print(my_list)
print(my_list[0]) # print first item
print(my_list + [10, 11]) # concatenation
print(len(my_list)) # length of list
print(my_list[0:2]) # slicing [0:n] of the list, starts from 0 and ends with n-1
print('hello' in my_list) # check whether that item exists in the list
print(my_list*2) # repetition of items in the list
my_list[0] = 100 # item assignment
print(my_list)

# lists methods 
myList = [1, 3, True, 10.5]
print(myList)
print("\n") 

myList.append("False") # alist.append(item) : adds item to the end of the list
print(myList)
print("\n") 

myList.insert(1, 15) # alist.insert(i, item) : inserts item in ith position in the list
print(myList)
print("\n") 

print(myList.pop()) # alits.pop() : removes and returns the last item in the list
print(myList)
print("\n")

myList.sort() # alist.sort() : modifies the list to be sorted
print(myList)
print("\n") 

myList.reverse() # alist.reverse() : modifies the list to be in reverse order
print(myList)
print("\n") 
 
print(myList.index(3)) # alist.index(item) : returns the index of the first occurrence of the item in the list
print("\n") 

print(myList.count(10.5)) # alist.count(item) : returns the number of occurences of the item in list
print("\n")

myList.remove(3) # alist.remove(item) : removes the first occurance of the item
print(myList)
print("\n")
 
del myList[2] # del alist[i] : removes item in the ith position
print(myList)

# range() with lists
print(range(5))
print(list(range(5)))
print("\n")

print(range(5, 10))
print(list(range(5, 10)))
print("\n")

print(range(1, 10, 2))
print(list(range(1, 10, 2)))
print("\n")

print(range(10, 1, -1))
print(list(range(10, 1, -1)))
print("\n")



# lists are mutable(changeable)