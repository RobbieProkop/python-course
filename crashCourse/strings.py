# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods

# name = "Robbie"
# age = 28



# String Formatting
# Concat
# print("Hello, my name is " + name)
# print("Hello, my name is {0}".format(name))
# print("Hello, my name is " + name + " and I am " + str(age))
# print("Hello, my name is {0} and I am {1}".format(name, age))
# print(f"Hello, my name is {name} and I am {age}")

# String Methods
s = 'hello world'
# s = 'HELLO WORLD'

# Capitalize
# first capitalize
# print(s.capitalize())

# all uppercase
# print(s.upper())

# all lowercase
# print(s.lower())

# swap current (if lower=>upper, if upper=>lower)
# print(s.swapcase())

# gets the length
# print(len(s))

# # Replace
# print(s.replace("world", 'everyone'))

# # Count
# sub="h"
# print(s.count(sub))

# # Starts with
# print(s.startswith('hello'))

# # ends with
# print(s.endswith('world'))

# split into a list
# print(s.split())

# find position (index)
# print(s.find('r'))

# is all alphanumeric
print(s.isalnum()) #currently false because of the space

# is all alphabetic
print(s.isalpha())

# is all numeric
print(s.isnumeric())
