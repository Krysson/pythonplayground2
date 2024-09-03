# VARIABLES

# x = 2
# y = 3
# z = x + y

# print(z)

# FUNCTIONS

# def say_hello(name="Mike"):
#   print(f'Hello {name}')

# say_hello()

# DICTIONARIES

person = {
  'first_name': 'Mike',
  'last_name': 'Smith',
  'age': 47
}

people = [
  {'first_name': 'Mike', 'age': 47},
  {'first_name': 'Kevin', 'age': 29 }
]

# person['phone'] = '555-555-5555'

# print(person['first_name'])
# print(person.get("last_name"))

# print(person.get('phone'))

# name = 'Mike'
# age = 47

print(f'Hello {people[1]["first_name"]}, you are {people[0]["age"]} years old')

# # FILES

# # Python has functions for creating, reading, updating, and deleting files.

# # Open a file
# myFile = open('myfile.txt', 'w')

# # Get some info
# print('Name: ', myFile.name)
# print('Is Closed : ', myFile.closed)
# print('Opening Mode: ', myFile.mode)

# # Write to file
# myFile.write('I love Python')
# myFile.write(' and JavaScript')
# myFile.close()

# # Append to file
# myFile = open('myfile.txt', 'a')
# myFile.write(' I also like PHP')
# myFile.close()

# # Read from file
# myFile = open('myfile.txt', 'r+')
# text = myFile.read(100)
# print(text)

#JSON
# JSON is commonly used with data APIS. Here how we can parse JSON into a Python dictionary

import json

#  Sample JSON
userJSON = '{"first_name": "John", "last_name": "Doe", "age": 30}'

# Parse to dict
user = json.loads(userJSON)

# print(user)
print(user['first_name'])

car = {'make': 'Ford', 'model': 'Mustang', 'year': 1970}

carJSON = json.dumps(car)

print(carJSON)