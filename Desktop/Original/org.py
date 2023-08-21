# a = 1
# print(a)


# # count = 0
# # while count < 9:
# #     print('the count;', count )
# #     count += 1
# print('goodbye')


# for x in 'geeksforgeeks':
#             if x!= 'k' and x!= 's':
#                 print(x)

# def tripflow(destination):
#         print('it is good')

# tripflow('kampala')


# def cal_taxi_price(price,rate, discount = 5):
#     print(price * rate * discount)

# cal_taxi_price(2,3)


def cal_taxi_price(us_dollars,exchange_rate):
    return us_dollars * exchange_rate

# a = cal_taxi_price(4, 5)

# print("this is the;", a)
# b = 3
# print(b)
# d = 4
# print(d)

# by = {
#     "a" : 1,
#     "b": 2,
#     "c": 3
# }

# print(by["a"])


# def highest_num(a):
#     return max(a)

# max_num = highest_num([1,5,3])
# print(max_num)


# -------------------------------------------------
def squared_numbers(numbers):
    dicti = {}
    count = 0

    for number in numbers:
        key = number
        value = number * number
        count = count + 1
        dicti[key] = value
    return dicti


result = squared_numbers(range(5,16))
print(result)



# ------------------------------------------------
# import numpy as np
# tuple1 = ((1,2,3),(4,5,6))
# array1 = np.array(tuple1)
# print(array1)



