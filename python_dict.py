"""
1. Sum Values
Write a function named sum_values that takes a dictionary named my_dictionary as a parameter.
The function should return the sum of the values of the dictionary
"""

def sum_values(my_dictionary):
    return sum(my_dictionary.values())

print(sum_values({"milk": 5, "eggs": 2, "flour": 3}))
print(sum_values({10: 1, 100: 2, 1000: 3}))

"""
2. EvenKeys
Create a function called sum_even_keys that takes a dictionary named my_dictionary, with all integer keys and values, 
as a parameter. This function should return the sum of the values of all even keys.
"""

def sum_even_keys(my_dictionary):
    sum = 0
    for key in my_dictionary:
        if key % 2 == 0:
            sum += my_dictionary[key]
    return sum

print(sum_even_keys({1: 5, 2: 2, 3: 3}))
print(sum_even_keys({10: 1, 100: 2, 1000: 3}))

"""
3. Add Ten
Create a function named add_ten that takes a dictionary with integer values named my_dictionary as a parameter. 
The function should add 10 to every value in my_dictionary and return my_dictionary
"""

def add_ten(my_dictionary):
    result_dictionary = {}
    for key_number in my_dictionary:
        adding_dictionary = {key_number: my_dictionary[key_number] + 10}
        result_dictionary.update(adding_dictionary)
    return result_dictionary

print(add_ten({1: 5, 2: 2, 3: 3}))
print(add_ten({10: 1, 100: 2, 1000: 3}))

"""
4. Values That Are Keys
Create a function named values_that_are_keys that takes a dictionary named my_dictionary as a parameter. 
This function should return a list of all values in the dictionary that are also keys.
"""

def values_that_are_keys(my_dictionary):
    values_that_keys = []
    for value in my_dictionary.values():
        for key in my_dictionary:
            if value == key:
                values_that_keys.append(value)
    return values_that_keys

print(values_that_are_keys({1: 100, 2: 1, 3: 4, 4: 10}))
print(values_that_are_keys({"a": "apple", "b": "a", "c": 100}))

"""
5. Largest 
Write a function named max_key that takes a dictionary named my_dictionary as a parameter. 
The function should return the key associated with the largest value in the dictionary.
"""

def max_key(my_dictionary):
    maximum = (max(my_dictionary.values()))
    for key_number in my_dictionary:
        if my_dictionary[key_number] == maximum:
            return key_number

print(max_key({1: 100, 2: 1, 3: 4, 4: 10}))
print(max_key({"a": 100, "b": 10, "c": 1000}))