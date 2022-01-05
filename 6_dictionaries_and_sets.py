my_list = [1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7]
print("0 in my_list =", 0 in my_list)

my_dictionary = {
    "name": "Adithya Visnu Prasetyo Putra =",
    "age": 25,
    "hobbies": ("coding =", "relaxing")
}
print("my_dictionary =", my_dictionary)
print("my_dictionary[\"age\"] =", my_dictionary["age"])

my_dictionary["address"] = "Cimahi"
print("my_dictionary =", my_dictionary)

del my_dictionary["hobbies"]
print("my_dictionary =", my_dictionary)

print("len(my_dictionary) =", len(my_dictionary))
print("\"name\" in my_dictionary =", "name" in my_dictionary)
print("my_dictionary.keys() =", my_dictionary.keys())
print("my_dictionary.values() =", my_dictionary.values())
print("my_dictionary.items() =", my_dictionary.items())

my_table_dictionary = {
    "name": ["Adithya =", "Visnu"],
    "age": [25, 25]
}
print("my_table_dictionary =", my_table_dictionary)


my_set = {1,3,5,7,9,7,5}
print("my_set =", my_set)
print("type(my_set) =", type(my_set))

my_set.add(11)
print("my_set =", my_set)

my_set.remove(7)
print("my_set =", my_set)
print("len(my_set) =", len(my_set))
print("min(my_set) =", min(my_set))
print("max(my_set) =", max(my_set))
print("sum(my_set) =", sum(my_set))
print("6 in my_set =", 6 in my_set)

my_second_set = {1,2,3,4,5}
print("my_set.union(my_second_set) =", my_set.union(my_second_set))
print("my_set.intersection(my_second_set) =", my_set.intersection(my_second_set))
print("my_set.difference(my_second_set) =", my_set.difference(my_second_set))
print("my_second_set.difference(my_set) =", my_second_set.difference(my_set))
print("my_set.issubset(my_second_set) =", my_set.issubset(my_second_set))
print("my_second_set.issubset(my_set) =", my_second_set.issubset(my_set))
print("{1,3}.issubset(my_set) =", {1,3}.issubset(my_set))


print("set(my_list) =", set(my_list))