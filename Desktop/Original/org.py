
1. 

# count = 0
# while count < 9:
# print('the count;', count )
# count += 1
# print('goodbye')


# -------------------------------------------------
2. 
"""
Write a Python program to get a string made of the first 2
and last 2 characters of a given string. If the string length is less than 2, return the empty string instead."""
# Sample String : 'w3resource'

# def string_test(items):
#         if len(items) > 2:
#             return items[:2] + items[-2:]
#         else:
#             return ""
        
# result = string_test('w3resource')
# print(result)


# ---------------------------------------------
3. 
"""
Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string 
already ends with 'ing', add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged"""

# def string_check(item):
#     if item[-3:] == "ing":
#         return item + "ly"
#     elif len(item) > 3:
#         return item + "ing"
#     else:
#         return item

# result = string_check('w3resource')
# print(result)



# -----------------------------------------------------------
4. 
"""
Write a Python function that takes a list of words and return
 the longest word and the length of the longest one"""

def longest_length(items):
    length = 0
    name = ''
    for item in items:
        result = len(item)
        if result > length:
             length = result
             name = item
    return { 'longest_word' : name,
            'longest length' : length

    }

results = longest_length(['book','sample', 'expect', 'scenerios', 'juggle'])
print(results)

# -------------------------------------------------------------
5.  
"""
Write a Python program to convert a given string into a list of words.
['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog.']
['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog.']"""


def convert_list(item):
    items = item.split(' ')
    return items


results = convert_list('The quick brown fox jumps over the lazy dog')
print(results)



# ------------------------------------------------------------------
6. 
"""
Write a Python program to check whether a given string contains a capital letter, 
a lower case letter, a number and a minimum length"""

def confirm(items):
    for item in items:
        if item.isupper():
            return "upper"
        elif item.islower():
            return "lower"
        elif item.isdigit():
            return "digit"
        

results = confirm('W3resource')
print(results)
        

# ------------------------------------------------------------------
7. 
'Write a Python program to remove duplicate words from a given string'

def duplicated(items):
    list_of_items = []
    for item in items:
        if item not in list_of_items:
            list_of_items.append(item)


    return " ".join(list_of_items)
        
results = duplicated(["Python Exercises Practice Solution Exercises"])
print(results) 

# ------------------------------------------------------------------
7. 
'Write a Python program to insert space before every capital letter appears in a given word.'
def seperator(items):
    result = ""
    for item in items:
        if item.isupper():
            result = result + " " + item.upper()
        else:
            result = result + item
    return result

a = seperator("PythonExercises")
print(a) 


# ------------------------------------------------------------------
7. 
"Write a Python program to print a specified list after removing the 0th, 4th and 5th elements."
def remove_elements(item):
    del item[5]
    del item[4] 
    del item[0]
    return item

result = remove_elements(['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow'])
print(result) 

# ------------------------------------------------------------------
8.
"""
Write a Python program to convert a list of multiple integers into a single integer."""
def intergers_(items):
    single_integer = int("".join(map(str, items)))
    print(single_integer)






intergers_([11, 33, 50])
print(result)