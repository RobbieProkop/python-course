# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.

# Create Tuple
fruits = ("Apples", "Bananas", "Mangos", "Blueberries")
# fruits2 = tuple(("Apples", "Bananas", "Mangos", "Blueberries"))

# single value tuple needs a trailing comma
fruits2 = ("Apples",)

# print(fruits[1])


# print(fruits2, type(fruits2))

# cannot change tuple value
# fruits[0] = ("Pears")

# delete tuple
del fruits2

# get length 
# print(len(fruits))



# A Set is a collection which is unordered and unindexed. No duplicate members.

# create a set
fruits_set= {"Apples", "Bananas", "Mangos"}

# check if in set
print("Apples" in fruits_set)

# Add to set to beginning
fruits_set.add("Grape")

# remove from set
fruits_set.remove("Grape")


# clear set entirely
fruits_set.clear()

del fruits_set
print(fruits_set)