# A List is a collection which is ordered and changeable. Allows duplicate members.
numbers = [1, 2, 3, 4, 5]
fruits = ["apples", "oranges", "bananas", "pears"]

#  use a constructor
# numbers2 = list((1,2,3,4,5))

# print(numbers, numbers2)

# get a value
# print(fruits[1])

#  lenght of list
# print(len(fruits))

# Append to end of list
# fruits.append("mangos")

# remove from lsits
# fruits.remove("apples")

# Insert to specific index
fruits.insert(2, "grapes")

# CHange value
fruits[0] = "blueberries"

# remove from specific index
fruits.pop(2)

# reverse list
fruits.reverse()

# sort alphabetically
fruits.sort()

# reverse sort
fruits.sort(reverse=True)

print(fruits)