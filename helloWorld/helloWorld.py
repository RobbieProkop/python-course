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
# a=12 
# b=3
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

# parrot = "Norwegian Blue"
# print(parrot)
# print(parrot[3])

# result = "we win"
# for i in result:
#   print(i)
# we win with indexing
# print(parrot[3])
# print(parrot[4])
# print(parrot[9])
# print(parrot[3])
# print(parrot[6])
# print(parrot[8])

# negative indexing
# print(parrot[-11])
# print(parrot[-1])
# print(parrot[-5])
# print(parrot[-11])
# print(parrot[-8])
# print(parrot[-6])

#  slices - :::
# print(parrot[0:6]) #start to end, does not include end
# print(parrot[:6]) #start defaults to 0
# print(parrot[10:]) #without end number, defaults to end 
# print(parrot[0:6:2]) # start at 0, goes to 6, steps of 2
# number = "9,233,372,036,854,775,807"
# number = "9,233;372:036 854,775;807"
# print(number)
# seperators = number[1::4]
# print(seperators)

# values = "".join(char if char not in seperators else " " for char in number).split()

# print(values)
# print([int(val) for val in values])

# letters = "abcdefghijklmnopqrstuvwxyz"
# letters = ""
# # python idiom
# backwards = letters[25::-1]
# print(backwards)
# # slice to get qpo
# back = letters[16:13:-1]
# print(back)
# # slice to get edcba
# back = letters[4::-1]
# print(back)
# # slice to produce last 8 characters in reverse order
# # back = letters[25:17:-1]
# back = letters[:-9:-1]
# print(back)

# # return last n items
# print(letters[-4:])
# print(letters[:1])
# print(letters[0])

# age = 28
# print("my age is {0}".format(age))

# for i in range(1,13):
  # print("No. {0} squared is {1} and cubed is {2}".format(i, i**2, i**3))
  # right aligned 
  # print("No. {0:2} squared is {1:3} and cubed is {2:4}".format(i, i**2, i**3))
  # # left aligned <
  # print("No. {0:<2} squared is {1:<3} and cubed is {2:<4}".format(i, i**2, i**3))
  # center aligned
  # print("No. {0:^2} squared is {1:^3} and cubed is {2:^4}".format(i, i**2, i**3))
  
# print("Pi is approx {0:12}".format(22/7))
# print("Pi is approx {0:12f}".format(22/7))
# print("Pi is approx {0:12.50f}".format(22/7))
# print("Pi is approx {0:52.50f}".format(22/7))
# print("Pi is approx {0:62.50f}".format(22/7))
# print("Pi is approx {0:<72.50f}".format(22/7))
# print("Pi is approx {0:<72.54f}".format(22/7))
  
  
# age = 24
# name = "Robbie"
# # f string is the same as format
# print(name + f" is {age} years old")
# print(f"Pi is approx {22/7:12.50f}")
# pi = 22/7
# print(f"Pi is approx {pi:12.50f}")