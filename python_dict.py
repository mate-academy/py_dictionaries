"""
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
#print(check_for_name("My name is Jamie", "Jamie"))
# should print True
#print(check_for_name("My name is jamie", "Jamie"))
# should print True
#print(check_for_name("My name is Samantha", "Jamie"))
# should print False



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
#print(max_key({"a":100, "b":10, "c":1000}))
# should print "c"
