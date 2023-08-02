# tuples : list are mutable but tuples are not

courses_tuple1 = ('algorithme', 'base de donnee', 'structure machine', 'outils de programmation', 'algorithme')

courses_tuple2 = courses_tuple1
print(courses_tuple1)
print(courses_tuple2)

# we can only to loop through and access : TypeError: 'tuple' object does not support item assignment
courses_tuple1[0] = 'Algo'

print(courses_tuple1[0])


