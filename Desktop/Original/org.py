
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



# ------------------------------------------------------------------
9.
"""
Write a Python program to convert a list to a list of dictionaries.
Sample lists: ["Black", "Red", "Maroon", "Yellow"], ["#000000", "#FF0000", "#800000", "#FFFF00"]"""

def dictionary_p(a, b):
    dicti = {}
    count = 0
    for item in a:
        key = item
        value = b[count]
        count = count + 1
        dicti[key] = value
    return dicti

result = dictionary_p(["Black", "Red", "Maroon", "Yellow"], ["#000000", "#FF0000", "#800000", "#FFFF00"] )
print(result) 


# ------------------------------------------------------------------
10.
"""
Write a Python program to calculate the sum of the numbers in a list between the indices of a specified range"""
items = [2, 1, 5, 6, 8, 3, 4, 9, 10, 11, 8, 12]
defined_items = items[4:9]

count = 0
for item in defined_items:
    count = count + item
print(count)



# ------------------------------------------------------------------
11.
"Write a Python script to add a key to a dictionary."

Sample_Dictionary = {0: 10, 1: 20}
Sample_Dictionary[2] = 30
print(Sample_Dictionary)


# ------------------------------------------------------------------
12.
"Write a Python script to concatenate the following dictionaries to create a new one"
dic1={1:10, 2:20}
dic2={3:30, 4:40}

dict1 = {**dic1, **dic2}

dic3={5:50,6:60}
dict1.update(dic3)

print(dict1)




# ------------------------------------------------------------------
13.

"""
Write a Python program to create a dictionary from a string.
Note: Track the count of the letters from the string.
Sample string : 'w3resource'"""
items = "w3resource"
unique_items = []
for item in items:
    if item not in unique_items:
        unique_items.append(item)
print(unique_items)

empty_dict = {}

for unique in unique_items:
    key = unique
    value = 0
    empty_dict[key] = value
print(empty_dict)


for unique in items:
    key = unique
    value = empty_dict[key] + 1
    empty_dict[key] = value
print(empty_dict)


# ------------------------------------------------------------------
14.
"""
 Write a Python program to count the number of characters (character frequency) in a string.
Sample String : google.com"""

#getting the unique items
items = "google.com"
empty_item = []
for item in items:
    if item not in empty_item:
        empty_item.append(item)
print(empty_item)

##setting the value to 0
empty_dict = {}
for unique in empty_item:
    key = unique
    value = 0
    empty_dict[key] = value
print(empty_dict)

#performing increment on the dictionary
dicti = {}
for item in items:
    key = item
    value = empty_dict[key] + 1
    empty_dict[key] = value
print(empty_dict)


# ------------------------------------------------------------------
15.


nums = [43, 20, 53, 12, 53, 5, 3, 2]
even = []
odd = []

for num in nums:
    if num % 2 == 0:
        even.append(num)
print(even)

for num in nums:
    if num % 2 != 0:
        odd.append(num)
print(odd)



# -----------------------------------------------------------------------
orders = [
    {
        'customer': 'Anita',
        'pickup':'ikeja',
        'destination':'vi',
        'amount': 1500,
        'status':'pending',
        'paymentMode' :'cash',
        'month': 'October'
    },
    {
        'customer': 'Mary',
        'pickup':'ogba',
        'destination':'bariga',
        'amount': 2500,
        'status':'delivered',
        'paymentMode' :'transfer',
        'month': 'July'
    },
    {
        'customer': 'Kola',
        'pickup':'badagri',
        'destination':'Sabo',
        'amount': 5500,
        'status':'delivered',
        'paymentMode' :'cash',
        'month': 'May'
    },
    {
        'customer': 'Kola',
        'pickup':'VI',
        'destination':'Mende',
        'amount': 2500,
        'status':'pending',
        'paymentMode' :'cash',
        'month': 'December'
    },
     {
        'customer': 'Mary',
        'pickup':'Ikorodu',
        'destination':'Ogba',
        'amount': 1500,
        'status':'delivered',
        'paymentMode' :'transfer',
        'month': 'December'
    },
     {
        'customer': 'Victor',
        'pickup':'Yaba',
        'destination':'Oyinbo',
        'amount': 1500,
        'status':'pending',
        'paymentMode' :'cash',
        'month': 'Febuary'
    },
    {
        'customer': 'Anita',
        'pickup':'Yaba',
        'destination':'Oyinbo',
        'amount': 2500,
        'status':'delivered',
        'paymentMode' :'cash',
        'month': 'August'
    },
     {
        'customer': 'Victor',
        'pickup':'VI',
        'destination':'Sabo',
        'amount': 5500,
        'status':'delivered',
        'paymentMode' :'transfer',
        'month': 'Sepetember'
    },
     {
        'customer': 'Mary',
        'pickup':'Ojota',
        'destination':'Sabo',
        'amount': 3500,
        'status':'pending',
        'paymentMode' :'cash',
        'month': 'Sepetember'
    },
     {
        'customer': 'Tosin',
        'pickup':'Ketu',
        'destination':'Sabo',
        'amount': 5500,
        'status':'delivered',
        'paymentMode' :'transfer',
        'month': 'Febuary'
    },
     {
        'customer': 'Mary',
        'pickup':'Ikorodu',
        'destination':'VI',
        'amount': 2500,
        'status':'delivered',
        'paymentMode' :'cash',
        'month': 'July'
    },
     {
        'customer': 'Mary',
        'pickup':'Ojota',
        'destination':'Maryland',
        'amount': 1500,
        'status':'pending',
        'paymentMode' :'cash',
        'month': 'May'
    },
    {
        'customer': 'Victor',
        'pickup':'Mowe',
        'destination':'Sabo',
        'amount': 10500,
        'status':'pending',
        'paymentMode' :'transfer',
        'month': 'March'

    },
     {
        'customer': 'Bola',
        'pickup':'Ogba',
        'destination':'Ikorodu',
        'amount': 500,
        'status':'pending',
        'paymentMode' :'cash',
        'month': 'January'
    },
     {
        'customer': 'Anita',
        'pickup':'VI',
        'destination':'Sabo',
        'amount': 1500,
        'status':'delivered',
        'paymentMode' :'cash',
        'month': 'January'
    }
]
# -------------------------------------------------------------------

# What is the total number of orders
## What is the total number of orders per month
## What is the total revenue per month
## How many order came from each customer
## What is the total revenue per customer
## What is the total order per the status
## What is the total revenue made
## What is the total revenue per payment mode


1. # What is the total number of orders
print(len(orders))

# ---------------------------------------------------------------------------

2. # What is the total number of orders
unique_months = []
for unique_m in orders:
    if unique_m['month'] not in unique_months:
        unique_months.append(unique_m['month'])

#setting the total values to 0
empty_dict = {}
for months in unique_months:
    key = months
    value = 0
    empty_dict[key] = value


for unique_m in orders:
    key = unique_m['month']
    value = empty_dict[key] + 1
    empty_dict[key] = value
print(empty_dict)


# ---------------------------------------------------------------------------
3. # What is the total revenue per month
unique_months = []
for unique_m in orders:
    if unique_m['month'] not in unique_months:
        unique_months.append(unique_m['month'])
print(unique_months)

# setting the total values to 0
empty_dict = {}
for months in unique_months:
    key = months
    value = 0
    empty_dict[key] = value


for unique_m in orders:
    key = unique_m['month']
    value = empty_dict[key] + unique_m['amount']
    empty_dict[key] = value
print(empty_dict)

# ---------------------------------------------------------------------------


5. ## What is the total revenue per payment mode
unique_p_mode = []
for unique_p in orders:
    if unique_p['paymentMode'] not in unique_p_mode:
        unique_p_mode.append(unique_p['paymentMode'])


# setting the total values to 0
empty_dict = {}
for unique_m in unique_p_mode:
    key = unique_m
    value = 0
    empty_dict[key] = value


for unique_p in orders:
    key = unique_p['paymentMode']
    value = empty_dict[key] + unique_p['amount']
    empty_dict[key] = value
print(empty_dict)



# ---------------------------------------------------------------------------