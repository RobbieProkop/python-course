# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
# Read more about dictionaries at https://docs.python.org/3/tutorial/datastructures.html#dictionaries

# create a dict
# similar to JSON object
person = {
  "first_name": "Robbie",
  "last_name": "Prokop",
  "age": 28,
}

# using a contructor
# person2 = dict(
#   first_name= "Robbie",
#   last_name= "Prokop",
#   age= 28,
# )

# get a value
print(person['first_name'])
print(person.get('last_name'))

# add key value
person['phone'] = "123-456-7890"

# get dict keys
# print(person.keys())

# get dict items
print(person.items())

# Copy dict - similar to JS spread operator
person2 = person.copy()
person2['city'] = "Tbilisi"

# Remove Item
del(person["age"])
person.pop('phone')

# CLear
person.clear()

# length
print(len(person2))

# list of dictionaries
people = [
  {
    "name": "Yuli",
    "age": 36
  },
  {
    "name": "Bill",
    "age": 24
  }
]

print(people[1]['name'])

print(person)
# print(person, type(person))
# print(person2, type(person2))

