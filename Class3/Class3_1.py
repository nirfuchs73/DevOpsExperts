from PIL import Image, ImageDraw


# 1. Write the following code: a = 1/0;
# 2. Build a corresponding try-except block toavoid exception.
def func_1():
    try:
        a = 1 / 0
        print(a)
    except ZeroDivisionError as err:
        print(err)


# 3. Is the following code legal? yes
def func_2():
    try:
        x = 1
        print(x)
    finally:
        print('finally')


# 4. What exception types can be caught by thefollowing handler?
# Except:
# 5. What is wrong with using the above type ofexception handler?

# 6. What exceptions can be caught by the following handlers?
# except IOError
# except ZeroDivisionError
def func_6():
    try:
        file = open('test.txt', 'r')
        print(file.read())
    except IOError as err:
        print(err)

    try:
        x = 10/0
        print(x)
    except ZeroDivisionError as err:
        print(err)


# 7. Create a text file named “words.txt” programmatically
# 8. Write your name into the file
# 9. Read your file content and print it
# 10. Write Hebrew content into your text file and print its content programmatically.
def func_7():
    file = open('words.txt', 'w+', encoding='utf-8')  # 7
    file.write('nir')  # 8
    file.seek(0)  # 9
    print(file.read())

    file.write('ניר')  # 10
    file.seek(0)
    print(file.read())

    file.close()


# 11. Create an image from code (png file) Hint: use Pillow
def func_11():
    img = Image.new('RGB', (100, 100), color='green')
    d = ImageDraw.Draw(img)
    d.text((20, 20), 'Hello World', fill='yellow')
    img.save('pil_green.png')


def main():
    # func_1()
    # func_2()
    # func_6()
    # func_7()
    func_11()


if __name__ == "__main__":
    main()
