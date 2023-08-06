import numpy as np
# print(np.__version__)
fun_np = dir(np)
print(type(fun_np))
print('numpy library', np.__version__, 'contains', len(fun_np), 'functions')

my_list = [1, 2, 3, 4, 5]
my_array = np.array(my_list)

print(my_list)
print(my_array)
print('=' * 50)

# nd.array ==> number dimensional array
print(type(my_list))
print(type(my_array))

print('=' * 50)
# Accessing elements
print(my_list[0])
print(my_array[0])
print('=' * 50)
# Create vector , matrices
print(np.array(10))
print(np.array([10, 20, 30]))
# number of square bracket represent number of lines
arr1 = np.array([[10, 20, 30], [40, 50, 60]])
print(arr1)
print('=' * 50)
# create matrix 3 lines 4 columns
arr2 = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(arr2)
print('=' * 50)
# access element matrices
print('line 0', arr1[0])
print(arr1.shape)
print(arr1.size)
print('=' * 50)
print('line 0', arr2[0])
# print(len(arr2))
print('='*50)
# create matrix 3 lines 4 columns
arr2 = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])
print('dimension de arr2 :', arr2.shape)
print('line number : ', arr2.shape[0])
print('column number : ', arr2.shape[1])
print(arr2)
print(arr2[0][0:1])
My_range = np.arange(4)
print(My_range)





