# tuples : list are mutable but tuples are not

courses_tuple1 = ('algorithme', 'base de donnee', 'structure machine', 'outils de programmation', 'algorithme')

courses_tuple2 = courses_tuple1
print(courses_tuple1)
print(courses_tuple2)

# we can only to loop through and access : TypeError: 'tuple' object does not support item assignment
# courses_tuple1[0] = 'Algo'

print(courses_tuple1[0])

# Sets : don't care about order, sets didn't allow double items
courses_set1 = {'algorithme', 'base de donnee', 'structure machine'}
courses_set2 = {'algorithme', 'analyse', 'stat'}
print(courses_set1)
print(courses_set2)

# set do verification of exist item more efficiently than list and tuples
print('math' in courses_set1)

# sets operators : union etc etc
print(courses_set1.intersection(courses_set2))
print(courses_set1.union(courses_set2))

empty_list = []
empty_tuple = ()
empty_set = {}
print(empty_list)




