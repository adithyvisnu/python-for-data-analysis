import numpy as np

my_list = [1,2,3,4,5]

my_np_arr = np.array(my_list)

print(type(my_np_arr))
print(my_np_arr)

my_second_list = [4,2,5,8,0]
my_2d_np_arr = np.array([my_list, my_second_list])
print(my_2d_np_arr)
print(my_2d_np_arr.dtype)
print(my_np_arr.shape, my_np_arr.size)
print(my_2d_np_arr.shape, my_2d_np_arr.size)

identity_matrix = np.identity(3)
print(identity_matrix)

create_matrix = np.eye(3,4,1)
print(create_matrix)

one_matrix = np.ones(shape=[1,5])
print(one_matrix)

zero_matrix= np.zeros(shape=[4,5])
print(zero_matrix)

my_2d_np_arr_ones = np.array([my_np_arr, my_np_arr+6, my_np_arr+12])
print(my_2d_np_arr_ones)


print(my_2d_np_arr_ones[1,3])