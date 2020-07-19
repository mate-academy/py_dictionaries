def sum_values(my_dictionary):

    sum_values = my_dictionary.values()
    return sum(sum_values)

print(sum_values({10:1, 100:2, 1000:3}))

def sum_even_keys(my_dictionary):
    even = 0
    for value in my_dictionary.values():
        if value % 2 == 0:
            even += value
            return even



print(sum_even_keys({1: 5, 2: 2, 3: 3}))

def add_ten(my_dictionary):
    for  key,value in my_dictionary.items():
            my_dictionary[key] = value + 10

            return my_dictionary

print(add_ten({10:1, 100:2, 1000:3}))

def values_that_are_keys(my_dictionary):
    list = []
    for value in my_dictionary.values():
        for key in my_dictionary.keys():
            if key == value:
                list.append(key)
    return list

print(values_that_are_keys({1:100, 2:1, 3:4, 4:10}))

def max_key(my_dictionary):
    max_k = (max (my_dictionary.values()))
    for key in my_dictionary:
        if my_dictionary[key] == max_k:
            return key

print(max_key({1:100, 2:2000, 3:4, 4:10}))



