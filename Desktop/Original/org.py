
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

