country_capitals = {"Uganda": "Kla", "Kenya": "Nairobi", "Rwanda": "Kigali", "Ghana": "Accra"}

country_capitals["Tanzania"] = "Dar es Salaam" # add key/value pair
print(country_capitals)
print("\n")

print(country_capitals["Uganda"])
print("\n")

print("China" in country_capitals) # check if key exists

#  methods
print(country_capitals.keys()) # returns all keys of the dict
print(list(country_capitals.keys())) # returns all keys as list
print("\n")


print(country_capitals.values()) # returns all values of the dict
print(list(country_capitals.values())) # returns all values as list
print("\n")

print(country_capitals.items()) # retuns key_value pairs in dict
print("\n")

print(country_capitals.get("France")) # retuns value associated with the key: France, None if doesnt exist
print(country_capitals.get("German"), "German not in dict") # default the value in the else part
print("\n")

#  unpack dict
for i in country_capitals: # prints keys
    print(i)

for i in country_capitals:
    print("The capital of " + i + " is " + country_capitals[i])

for i, j in country_capitals.items():
    print("The capital of " + i + " is " + j)