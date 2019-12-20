import os
import datetime


# 1. Write a program which prints 'Hello' on screen and then print your name on a separate line.
def print_name(name):
    # name = inputname('Enter name:')
    print('Hello')
    print(name)


# 2. Write a program to print the sum of two numbers
def sum(num1, num2):
    return num1 + num2


# 3. Write a program which will print the Python version number installed on your machine.
def print_version():
    os.system('python --version')


# 4. Write a program which will reverse a word (e.g. hello -> olleh)
def reverse(str):
    return str[::-1]
    # return res


# 5. Write a program which will print the amount of letters in a given word (e.g. hello -> 5)
def print_length(str):
    print(len(str))


# 6. Write a program which will print the current date and time
def print_date():
    print(datetime.datetime.now())


# 7. Write a program which:
# A. contains 2 variables X & Y
# B. Give X & Y values (e.g. X = 1, Y = 5)
# C. Using if-else check which is bigger, and print the bigger number.
def print_bigger():
    x = 9
    y = 3
    if x > y:
        print('x is bigger')
    elif x < y:
        print('y is bigger')
    else:
        print('equal')


# 8. Write a program which will check whether or not the number 120 is bigger than 5 and smaller than 200, if so, print MATCH
def is_match(num):
    if num > 5 and num < 200:
        print('MATCH')
    else:
        print('NO MATCH')


print_name('nir')
print(sum(2, 4))
print_version()
print(reverse('1234'))
print_length('hello')
print_date()
print_bigger()
is_match(120)
