first_list = ['lesson', 5, True]
print("first_list", first_list)

second_list = list('life is study')
print("second_list", second_list)

third_list = []
print("third_list", third_list)

third_list.append('an element')
print("third_list", third_list)

first_list.remove(5)
print("first_list", first_list)

combined_list = first_list + second_list
print("combined_list", combined_list)

combined_list.extend(third_list)
print("combined_list", combined_list)

numbers = [1, 3, 5, 7, 9, 1]
print("len(numbers)", len(numbers))
print("max(numbers)", max(numbers))
print("min(numbers)", min(numbers))
print("sum(numbers)", sum(numbers))
print("sum(numbers)/len(numbers)", sum(numbers)/len(numbers))

print("2 in numbers", 2 in numbers)
print("2 not in numbers", 2 not in numbers)
print("numbers.count(1)", numbers.count(1))

unsorted_numbers = [3, 2, 5, 1, 4]
unsorted_numbers.reverse()
print("unsorted_numbers", unsorted_numbers)

unsorted_numbers.sort()
print("unsorted_numbers", unsorted_numbers)

list_of_string = ["hello", "my friend", "my name", "is", "Adith"]
print("list_of_string[1]", list_of_string[1])
print("list_of_string[-1]", list_of_string[-1])
print("list_of_string[-3]", list_of_string[-3])
# print("list_of_string[5]", list_of_string[5])

nested_list = [[1,2,3], [2,3,4], [4,5,6]]
print("nested_list", nested_list)
print("nested_list[0]", nested_list[0])
print("nested_list[2][1]", nested_list[2][1])

slice = unsorted_numbers[1:3]
print("slice", slice)

slice_every_n = unsorted_numbers[0:6:3]
print("slice_every_n", slice_every_n)

slice_to_n = unsorted_numbers[:3]
print("slice_to_n", slice_to_n)

slice_from_n = unsorted_numbers[3:]
print("slice_from_n", slice_from_n)

copy_list = unsorted_numbers[:]
print("copy_list", copy_list)

del copy_list[2]
print("copy_list", copy_list)

popped_list = copy_list.pop()
print("popped_list", popped_list)
print("copy_list", copy_list)


copy_unsorted_numbers = unsorted_numbers.copy()
copy_unsorted_numbers.append(6)
print("unsorted_numbers", unsorted_numbers)
print("copy_unsorted_numbers", copy_unsorted_numbers)