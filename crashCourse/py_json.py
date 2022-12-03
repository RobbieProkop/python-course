# JSON is commonly used with data APIS. Here how we can parse JSON into a Python dictionary

import json

# sample JSON (pretend this comes from some API)
userJSON = '{"first_name": "Robbie","last_name": "Prokop", "age": 28}'

# parse to dict
user = json.loads(userJSON)


# print(user)
# print(user['first_name'])

# Turn DIctionary into JSOn
car = {'make': 'Ford', 'model': 'GT', 'year': 1967}

carJSON = json.dumps(car)

print(carJSON)