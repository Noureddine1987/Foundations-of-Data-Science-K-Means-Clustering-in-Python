# comparison : == , !=, <, >, <=, >=, is ==> object identity
if True:
    print('condition was true')

# didnt reach the condition
if False:
    print('condition wasnt  met')

# condition
language = 'java'
if language == 'python':
    print('language is python')
elif language == 'java':
    print('language is java')
else:
    print('no match')

# boolean operations : and or not
user = 'admin'
logged_in = True
if user == 'admin' and logged_in:
    print('admin page')
else:
    print('bad connexion')

if not logged_in:
    print('please log in ')
else:
    print('welcome')

# is : object identity example
a = [1, 2, 3]
b = [1, 2, 3]
print(a is b)
print(id(a))
print(id(b))









