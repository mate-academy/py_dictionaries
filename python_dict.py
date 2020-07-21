"""
<<<<<<< HEAD
1. Sum Values
Write a function named sum_values that takes a dictionary named my_dictionary as a parameter.
The function should return the sum of the values of the dictionary
"""
# Write your sum_values function here:
def sum_values(my_dictionary):
    return sum(my_dictionary.values())

# Uncomment these function calls to test your sum_values function:
print(sum_values({"milk":5, "eggs":2, "flour": 3}))
# should print 10
print(sum_values({10:1, 100:2, 1000:3}))
# should print 6
=======
1. Count Letters
Write a function called unique_english_letters that takes the string word as a parameter. The function should return the total number of unique letters in the string. Uppercase and lowercase letters should be counted as different letters.
We’ve given you a list of every uppercase and lower case letter in the English alphabet. It will be helpful to include that list in your function.
 
#Write your function here
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
def unique_english_letters(word):
 counter = 0
 for i in letters:
       if i in word:
           counter += 1
 return counter
print(unique_english_letters("mississippi"))
# should print 4
print(unique_english_letters("Apple"))
# should print 4
>>>>>>> 3efa2953ab0a2ce8962a006b3e72e27306b5404c


"""
2. Count X
Write a function named count_char_x that takes a string named word and a single character named x as parameters. The function should return the number of times x appears in word.
# Write your count_char_x function here:
def count_multi_char_x(word, phrase):
 wc = 0
 y=word.find(phrase)
 if y > -1:
   x=y+3
   wc += 1
   yeniword =word[x:]
   z = yeniword.find(phrase)
   if z > -1:
     wc += 1
 return wc
# Uncomment these function calls to test your tip function:
#print(count_char_x("mississippi", "s"))
# should print 4
#print(count_char_x("mississippi", "m"))
# should print 1

<<<<<<< HEAD
# Write your sum_even_keys function here:
def sum_even_keys(my_dictionary):
    sum = 0
    for key in my_dictionary:
        if key % 2 == 0:
            sum += my_dictionary[key]
    return sum
# Uncomment these function calls to test your  function:
print(sum_even_keys({1:5, 2:2, 3:3}))
# should print 2
print(sum_even_keys({10:1, 100:2, 1000:3}))
# should print 6
=======

"""
3. Write a function named count_multi_char_x that takes a string named word and a string named x. This function should do the same thing as the count_char_x function you just wrote - it should return the number of times x appears in word. However, this time, make sure your function works when x is multiple characters long.
For example, count_multi_char_x("Mississippi", "iss") should return 2
# Write your count_multi_char_x function here:
def count_multi_char_x(word, x):
 count = 0; c = 0
 for w in range(len(word)):
   c += 1
   if word[w : w + len(x)] == x:
     count += 1
 return count, c
# Uncomment these function calls to test your function:
#print(count_multi_char_x("mississippi", "iss"))
# should print 2
#print(count_multi_char_x("apple", "pp"))
# should print 1
>>>>>>> 3efa2953ab0a2ce8962a006b3e72e27306b5404c


"""
4. Check Name
Write a function called check_for_name that takes two strings as parameters named sentence and name. The function should return True if name appears in sentence in all lowercase letters, all uppercase letters, or with any mix of uppercase and lowercase letters. The function should return False otherwise.
For example, the following three calls should all return True:
# Write your check_for_name function here:
def check_for_name(sentence, name):
 return name.lower() in sentence.lower()
 return name.upper() in sentence.upper()
 return False
# Uncomment these function calls to test your  function:
<<<<<<< HEAD
#print(add_ten({1:5, 2:2, 3:3}))
# should print {1:15, 2:12, 3:13}
#print(add_ten({10:1, 100:2, 1000:3}))
# should print {10:11, 100:12, 1000:13}


"""
4. Values That Are Keys
Create a function named values_that_are_keys that takes a dictionary named my_dictionary as a parameter. 
This function should return a list of all values in the dictionary that are also keys.
"""
# Write your values_that_are_keys function here:
=======
#print(check_for_name("My name is Jamie", "Jamie"))
# should print True
#print(check_for_name("My name is jamie", "Jamie"))
# should print True
#print(check_for_name("My name is Samantha", "Jamie"))
# should print False
>>>>>>> 3efa2953ab0a2ce8962a006b3e72e27306b5404c



"""
5. Largest Value
Write a function named max_key that takes a dictionary named my_dictionary as a parameter. The function should return the key associated with the largest value in the dictionary.
# Write your max_key function here:
def max_key(my_dictionary):
 max_val = 0
 for key in my_dictionary.keys():
   for value in my_dictionary.values():
     if value > max_val:
       max_val = value
   if my_dictionary[key] == max_val:
       return key
# Uncomment these function calls to test your  function:
#print(max_key({1:100, 2:1, 3:4, 4:10}))
# should print 1
<<<<<<< HEAD
# print(max_key({"a":100, "b":10, "c":1000}))
# should print "c"
=======
#print(max_key({"a":100, "b":10, "c":1000}))
# should print "c"
>>>>>>> 3efa2953ab0a2ce8962a006b3e72e27306b5404c
