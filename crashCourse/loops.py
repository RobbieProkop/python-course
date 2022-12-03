# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
people = ["John", "Paul", "Jones"]

# simple for loop
# for person in people:
#   print(person)
  
# Break
# for person in people:
#   if person == "Paul":
#     break
#   print(person)
  
# Continue
# for person in people:
#   if person == "Paul":
#     print(f"{person} got skipped!")
#     continue
#   print(person)


# Range (does not do the final num in the range)
for i in range(len(people)):
  print(i)
  
# While loops execute a set of statements as long as a condition is true.
count = 0
while count <= 10:
  print(count)  
  count += 1