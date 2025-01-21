# sentence = "Python is fun"
# split = sentence.split() # split() method splits the string into a list
# print(split)

# join = " ".join(sentence) # join() method joins the elements of the provided list
# print(join)

# replace = sentence.replace("fun", "awesome") # replace() method replaces a string with another string
# print(replace)

# strip = "   Python is fun   ".strip() # strip() method removes any leading (spaces at the beginning) and trailing (spaces at the end) characters
# print(strip)

# def reverse_string(s):
#     return s[::-1]

# def count_vowels(s):
#     vowels = "aiueoAIUEO"
#     return sum([1 for c in s if c in vowels])

# def is_palindrome(s):
#     s = s.lower().replace(" ", "")
#     return s == s[::-1]

# #regular expressions
# import re
# text = "contact me at: 123-456-7890"
# digits = re.findall(r'\d+', text) # \d matches any digit
# print(digits)

# updated_text = re.sub(r'\d+', 'x', text) # sub() method replaces all occurrences of the RE pattern in string with repl, substituting all occurrences unless max provided
# print(updated_text)

# def clean_text(text):
#     #remove punctuation
#     text = re.sub(r"[^\w\s]", "", text)
#     #remove extra spaces
#     text = " ".join(text.split())
#     #convert to lowercase
#     return text.lower()
# input_text = ("   Hello, World!!! Welcome to PYTHon, Programming.... !!   ")
# cleaned_text = clean_text(input_text)
# print("Cleaned text:", cleaned_text)

# with open("sample.txt", "w") as file:
#     file.write("Hello, World!")
#     file.writelines(["Alice", "Bob", "Charlie"])
    
# try:
#     with open("sample.txt", "r") as file:
#         content = file.read()
# except FileNotFoundError:
#     print("File not found")
    
# #create a list of squares
# squares = [x**2 for x in range(10)]
# print(squares)

# #filter even/odd number
# evens = [x for x in range (10) if x % 2 ==0]
# print(evens)

# #lambda arguments: expression
# add = lambda x, y: x+y
# print(add(3,5))

# numbers = [1, 2, 3, 4]
# squares = map(lambda x: x**2, numbers)
# print(list(squares))

# #map() applies a function to all the items in an input_list
# def square(x):
#     return x**2
# numbers = [1, 2, 3, 4]
# squares = map(square, numbers)
# print(list(squares))

# #filter() method filters the given sequence with the help of a function that tests each element in the sequence to be true or not
# numbers = [1, 2, 3, 4]
# evens = filter(lambda x: x % 2 == 0, numbers)
# print(list(evens))

#reduce() function is defined in functools module
# from functools import reduce
# numbers = [1, 2, 3, 4]
# sum = reduce(lambda x, y: x+y, numbers)
# print(sum)

# #os module provides a way of using operating system dependent functionality
# import os
# print(os.getcwd())
# os.mkdir("test")
# os.remove("testos.txt")

#sys module provides access to some variables used or maintained by the interpreter and to functions that interact strongly with the interpreter
import sys
print(sys.argv)
print(sys.version)