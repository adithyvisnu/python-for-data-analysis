my_tuple = (1, 2, 3)
print(my_tuple)

my_list = [1,2,3,4,5,6,7]
convert_list_to_tuple = tuple(my_list)
print(convert_list_to_tuple)
print(convert_list_to_tuple[2:4])
print(len(convert_list_to_tuple))
print(max(convert_list_to_tuple))
print(min(convert_list_to_tuple))
print(sum(convert_list_to_tuple))

# convert_list_to_tuple.append tidak ada fungsi untuk penambahan beda dengan list
# del convert_list_to_tuple[1] tidak ada fungsi untuk pengurangan beda dengan list

# Strings ===== immutable sequences of characters

my_string = "Adithya Visnu"
print(my_string[3])
print(my_string[3:])
print(my_string[::-1])
print(len(my_string))
print(my_string.count('a'))

print(my_string.lower())
print(my_string.upper())
print(my_string.title())
print(my_string.find('x'))


print(my_string.replace('i', 'r'))
print(my_string.split())
print(my_string.split('a'))
print(my_string.split('z'))

my_long_string = """
    Hello there
    i was here
"""
print(my_long_string)
print(my_long_string.splitlines())
print(my_long_string.splitlines()[2])
print(my_long_string.splitlines()[2].strip())

# print("Bqu Rizka Canqtiqk".strip("q")) why not working

print("Hello " + "World")
print(', '.join(my_string))


template_string = "Hello my name is {} and I lived in {}"
print(template_string.format('adith', 'your memories'))

print(f"My name is {my_string}")