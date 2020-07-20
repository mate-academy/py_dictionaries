# Write your sum_values function here:
def sum_values(my_dictionary):
    sum_dict = 0
    for value in my_dictionary.values():
        sum_dict = sum_dict + value
    return sum_dict
# Uncomment these function calls to test your sum_values function:
print(sum_values({"milk": 5, "eggs": 2, "flour": 3}))
# should print 10
print(sum_values({10: 1, 100: 2, 1000: 3}))
# should print 6


# Write your sum_even_keys function here:
def sum_even_keys(my_dictionary):
    even_keys = 0
    for key, values in  my_dictionary.items():
        if key % 2 == 0:
            even_keys += values
    return even_keys
print("______________")
# Uncomment these function calls to test your  function:
print(sum_even_keys({1:5, 2:2, 3:3}))
# should print 2
print(sum_even_keys({10:1, 100:2, 1000:3}))
# should print 6


def add_ten(my_dictionary):
    for values in my_dictionary.keys():
        my_dictionary[values] = my_dictionary[values] + 10
    return my_dictionary
print("______________")
# Uncomment these function calls to test your  function:
print(add_ten({1:5, 2:2, 3:3}))
# should print {1:15, 2:12, 3:13}
print(add_ten({10:1, 100:2, 1000:3}))
# should print {10:11, 100:12, 1000:13}

