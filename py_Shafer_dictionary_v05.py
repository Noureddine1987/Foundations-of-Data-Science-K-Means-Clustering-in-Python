# dictionary handling :
student = {
    'name': 'Boukhari',
    'age': 36,
    'courses': ['algo', 'TIC']
}
print(student['name'])
print(student['courses'])
# not existed key  print(student['phone'])
print(student.get('name'))
# print None if not exist
print(student.get('courses'))
print(student.get('phone'))
# print msg if not exist
print(student.get('salary', 'not found'))
student['phone'] = '554959294'
print(student.get('phone', 'Not Found'))

# change somme keys values
student.update({'age': 35, 'courses': ['Matlab', 'Algo']})
print(student)

# delete a key
del student['phone']
print(student)

# print keys
print('print keys : ')
print(student.keys())
print('print keys with for loup : ')
for keys in student:
    print(keys)

# print values
print('print values : ')
print(student.values())
print('print values with for loops')
for values in student:
    print(values)

# print items (both)
print('print items : ')
print(student.items())
print('print items with for loop : ')
for key, values in student.items():
    print(key, values)
