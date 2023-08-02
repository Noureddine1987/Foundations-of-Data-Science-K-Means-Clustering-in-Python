# list
courses = ['algo', 'matlab', 'tic', 'numeric programing']
print(courses)


print('length of the list : ', len(courses))

print('second items in the list :', courses[1])

# acces to the list of the list by -1 index directly
print('last item of the list : ', courses[-1])

# print to or more items [first : last] ==> not including last ==> or [:last]
print('print 0 1 : ', courses[0:2])

# add one items to the list ==> to the index of the list ==> insert method insert(index, object)
print('insert BDD course to the list : ', courses.insert(3, 'BDD'))
print(courses)

# add a list in the index of other list [[newList], element1, element2]
courses_2 = ['Art', 'Education']
courses.insert(0, courses_2)
print(courses)
print('print the fits index which is the list courses_2 )) : ', courses[0])

# we want to add a values of the second list as element
courses.extend(courses_2)
print('extend courses with courses_2 : ', courses)

# remove item from the list
courses.remove('algo')
print('remove algo from the list : ', courses)

# remove item from the last fo the list ==> pop
courses.pop()
print(courses)

popped_item = courses.pop()
print('popped item from the list courses : ', popped_item)

# sort the list : reverse methode : the last become the first etc etc
print(courses)
courses.reverse()
print('reversed list ', courses)

# sort a list courses.sort() :
team = ['nori', 'ilyes', 'hafid', 'mokhtar']
numbers = [5, 6, 88, 9, 4]
team.sort()
numbers.sort()
print('sorted list : ', team)
print('sorted numbers : ', numbers)
numbers.sort(reverse=True)
print(numbers)

# min, max, sum
print('min of numbers : ', min(numbers))
print('max of numbers : ', max(numbers))
print('sum of numbers : ', sum(numbers))

# index of any item
print('index of nori : ', team.index('nori'))
print('index of hafid : ', team.index('hafid'))
# print('index of ali : ', team.index('ali'))
print('ali' in team)

print(numbers)
for it in numbers:
    print(it)

for index, course in enumerate(courses, start=1):
    print(index, course)

