# 1. Write a Python program to calculate the length of a string
def get_length(str):
    return len(str)


# Write a Python program to count the number of characters (character frequency) in a string
def count_chars(str):
    dict = {}
    for char in str:
        if not char in dict:
            dict[char] = 1
        else:
            dict[char] = dict[char] + 1
    return dict


# 3. Write a Python program to get a string made of the first 2 and the last 2 chars from a
# given a string. If the string length is less than 2, return instead of the empty string.
def first_last(str):
    if len(str) < 2:
        return ''
    return str[:2] + str[len(str)-2:]


# print(get_length('1111'))
# print(count_chars('google.com'))
print(first_last('w'))
