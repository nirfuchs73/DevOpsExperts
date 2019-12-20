# 1. Write a program to print numbers from 1 to 10.
def func_1():
    for x in range(1, 11):
        print(x)


# 2. Write a program which will get a number from the user a number and
# determine whether or not the number is positive or negative, by printing “+”
# (plus sign) for positive or “–“ (minus sign) for negative.
def func_2():
    num = int(input('Enter a number:'))
    if num > 0:
        print('+')
    elif num < 0:
        print('-')
    else:
        print('0')


# 3. Write a program which will get two numbers from the user and print the bigger number.
def func_3():
    num1 = int(input('Enter first number:'))
    num2 = int(input('Enter second number:'))
    if num1 > num2:
        print(num1)
    elif num1 < num2:
        print(num2)
    else:
        print('equal')


# 4. Write a program which will ask the user for his age and height, if user age
# is greater than 10 and his height is greater than 120, print: “Welcome to
# the rollercoaster”, if not, print: “Sorry.. maybe next time”
def func_4():
    age = int(input('Enter age:'))
    height = int(input('Enter height:'))
    if age > 10 and height > 120:
        print('Welcome to the rollercoaster')
    else:
        print('Sorry.. maybe next time')


# Write a program which will get two numbers from the user and determine
# whether or not the numbers are equal or not, by printing equal or not equal
def func_5():
    num1 = int(input('Enter first number:'))
    num2 = int(input('Enter second number:'))
    if num1 == num2:
        print('equal')
    else:
        print('not equal')


# 7. Create a program with a function named “get_name” which will receive a
# name and will print: “Your name” + the name.
def get_name(name):
    print('Your name: ' + name)


# 8. Create a program which will get a number and print true if the number is
# bigger than 100 or false if not.
def func_8(num):
    if num > 100:
        print(True)
    else:
        print(False)


def main():
    # func_1()
    # func_2()
    # func_3()
    # func_4()
    # func_5()
    # get_name('Nir')
    func_8(101)


if __name__ == "__main__":
    main()
