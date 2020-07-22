#Write a function named sum_values that takes a dictionary named my_dictionary as a parameter. The function should return the sum of the values of the dictionary
def sum_values (my_dictionary):
   sum = 0
   for i in my_dictionary.values():
       sum = sum + i
   return sum
my_dictionary = {"milk":5, "eggs":2, "flour": 3}
print(sum_values(my_dictionary))
my_dictionary = {10:1, 100:2, 1000:3}
print (sum_values(my_dictionary))

#Create a function called sum_even_keys that takes a dictionary named my_dictionary, with all integer keys and values, as a parameter. This function should return the sum of the values of all even keys.
def sum_even_keys (my_dictionary):
   count = 0
   for key in my_dictionary.keys():
       count += my_dictionary[key]
   return count
my_dictionary = {1:5, 2:2, 3:3}
print(sum_even_keys(my_dictionary))
my_dictionary = {10:1, 100:2, 1000:3}
print(sum_even_keys(my_dictionary))

#Create a function named add_ten that takes a dictionary with integer values named my_dictionary as a parameter. The function should add 10 to every value in my_dictionary and return my_dictionary
def add_ten(my_dictionary):
   for key in my_dictionary:
       my_dictionary[key] += 10
   return my_dictionary
my_dictionary = {1:5, 2:2, 3:3}
print(add_ten(my_dictionary))
my_dictionary = {10:1, 100:2, 1000:3}
print(add_ten(my_dictionary))

#Create a function named values_that_are_keys that takes a dictionary named my_dictionary as a parameter. This function should return a list of all values in the dictionary that are also keys.
def values_that_are_keys (my_dictionary):
   list1 = []
   for i in my_dictionary.values():
       if i in my_dictionary.keys():
           list1.append(i)
   return list1
my_dictionary = {1:100, 2:1, 3:4, 4:10}
print(values_that_are_keys(my_dictionary))
my_dictionary = {"a":"apple", "b":"a", "c":100}
print(values_that_are_keys(my_dictionary))

#Write a function named max_key that takes a dictionary named my_dictionary as a parameter. The function should return the key associated with the largest value in the dictionary.
def max_key (my_dictionary) -> object:
   max_key = 0
   for key,value in my_dictionary.items():
       if value > my_dictionary.get(max_key,0):
           max_key = key
   return max_key
my_dictionary = {1:100, 2:1, 3:4, 4:10}
print(max_key(my_dictionary))
my_dictionary = {"a":100, "b":10, "c":1000}
print(max_key(my_dictionary))
