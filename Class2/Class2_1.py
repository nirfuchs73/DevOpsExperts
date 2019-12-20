import array as array
import math


# A.
# 1. Create two variables name X and Y.
# 2. Print “BIG” if X is bigger than Y .
# 3. Print “small” if X is smaller than Y.
def func_a():
    x = 12
    y = 9
    if x > y:
        print('BIG')
    if x < y:
        print('SMALL')


# B.
# 1. Run a “for” loop 5 times.
# 2. Print iteration number every time.
def func_b():
    for x in range(5):
        print(x)


# C.
# 1. Create a variable and initialize it with a number 1-4.
# 2. Create 4 conditions (if-elif) which will check the variable.
# 3. print the season name accordingly:
def func_c():
    x = 4
    if x == 1:
        print('summer')
    elif x == 2:
        print('winter')
    elif x == 3:
        print('fall')
    elif x == 4:
        print('spring')


# D.
# 1. how many times will the following loop run? 10
# 2. what will be printed last? 10
def func_d():
    count = 1
    while count < 11:
        print(count)
        count = count + 1


# E.
# Write a program with variables holding the following:
# 1. Your age.
# 2. First letter of your last name.
# 3. Current shekels-dollar currency.
# 4. Did you flew abroad (true/false)
# 5. Your apartment number.
# ● Print all variables.
# ● Add the currency to your age, and check the result.
def func_e():
    age = 24
    lname = 'f'
    currency = 3.49
    flyAbroad = True
    apartmentNum = 113
    print(age, lname, currency, flyAbroad, apartmentNum)
    print(age + currency)


# F.
# Create a program which uses input with the following:
# 1. Ask user for his phone number
# 2. Print the words “phone number” and the phone number the user entered.
def func_f():
    phone_number = input('Emter phone number:')
    print('phone number:', phone_number)


# G.
#  Write a program with the following:
# 1. Method named printHello() that prints the word “hello”.
# 2. Method named calculate() which adds 5+3.2 and prints the result.
def print_hello():
    print('hello')


def calculate():
    res = 5 + 3.2
    print(res)


# H.
# Write a program with the following:
# 1. Method that receive your name and prints it.
# 2. Method that receive a number, divide it by 2, and prints the result.
def print_name(name):
    print(name)


def devide(num):
    print(num/2)


# I.
# Write a program with the following:
# 1. Method that receive two numbers, add them, and return the sum.
# 2. Method that receive two Strings, add space between them,
# and return one spaced string.
def add(num1, num2):
    return num1 + num2


def add_str(str1, str2):
    return str1 + ' ' + str2


# J.
# Create a program with the following:
# 1. Create an array with 3 numbers
# 2. Iterate through the array to print all elements.
def print_array():
    # arr = [1, 2, 3]
    arr = array.array('i', [1, 2, 3])
    for item in arr:
        print(item)


# K.
# Create a nested for loop (loop inside another loop) to create
# a pyramid shape:
def print_pyramid(num):
    for i in range(num):
        line = ''
        for j in range(i + 1):
            line += '#'
        print(line)


# L.
# Create a nested for loop to create X shape (width is 7, length is 7):
def print_x(num):
    for i in range(num):
        line = ''
        for j in range(num):
            if j == i or j == num - i - 1:
                line += '#'
            else:
                line += ' '
        print(line)


# M.
# Write a program with the following:
# 1. Method that gets a number from the user (using input).
# 2. Method that receive the number from the first method, and
# computes the sum of the digits the integer (e.g. 25 = 7, 2+5=7)
def get_num():
    return int(input('Enter number:'))


def computes():
    res = 0
    num = get_num()
    while num >= 1:
        res += num % 10
        num = math.floor(num / 10)

    return res


def main():
    # func_a()
    # func_b()
    # func_c()
    # func_d()
    # func_e()
    # func_f()
    # print_hello()
    # calculate()
    # print_name('nir')
    # devide(10)
    # print(add(4, 6))
    # print(add_str('Hello', 'World'))
    # print_array()
    # print_pyramid(7)
    # print_x(7)
    print(computes())


if __name__ == "__main__":
    main()
