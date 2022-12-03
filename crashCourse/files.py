# Python has functions for creating, reading, updating, and deleting files.

# open a file
myFile = open('myfile.txt', 'w')

# get info on file
print('Name: ', myFile.name)
print('is closed: ', myFile.closed)
print('Mode: ', myFile.mode)

# Write to file
myFile.write("I love programming")
myFile.write(' and hacking')
myFile.close()

#  append to file
myFile = open('myfile.txt', 'a')

myFile.write(" Appppeeennndedddd")
myFile.close()


# read from file
myFile = open('myfile.txt', 'r+')
text = myFile.read(100)
print(text)