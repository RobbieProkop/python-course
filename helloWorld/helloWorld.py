# Print
# print('Hello World!')
# print(1 + 2)
# print(7 * 6)
# print()
# print("The End", "or is it?", "another print", 2+4)

# Variables
# greeting = "Hello"
# name = "Robbie"
# name = input("Please enter your name ")

# print(greeting, name)

# Escaped Characters
# splitString = "This string have been \nsplit over \nseveral\nlines"
# print(splitString)

# tabbedString = "1\t2\t3\t4\t5"
# print(tabbedString)

# print('quote\'s being backslashed')
# # backslashed
# print("""quote\'s being "backslashed" """)

# TYPE OF 
# print(type(greeting))
# age = 28.67
# print(type(age))

# # age = "2 years"
# print("age",age)
# print(type(age))

# Cannot concat different data types
# print(name + " is " + age + " years old")

# Operators
a=12 
b=3
# print(a/b) #returns a float
# print(a//b) #returns an integer
# print(a%b) #remainder after integer division

# for i in range(1, 4): #start - end. start is included, end is not
#   print(i)
  
# for i in range(1, a/b): #float cannot be interpreted as int
#   print(i)
# for i in range(1, a//b): #successfull operation
#   print(i)

#  Operator Precedence
# print(a+b/3-4*12) # this equals -35.0. DIvision and multiplicaiton are more important.
# b / 3 = 1.0
# 4*12 = 48
#  12 + 1.0 - 48 = -35.0

# print(a +(b/3) - (4*12)) # this also equals -35.0

# print(((a+b)/3 -4) * 12)

# c = a+b
# d= c/3
# e = d-4
# print(e*12)

# print(a / (b*a) / b)

# parrot = "Parrot Parrot"
# print(parrot)
# print(parrot[3])

result = "we win"
for i in result:
  print(i)