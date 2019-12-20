import os
from docx import Document


# 1. Will the following code block cause an exception? If so, why? yes
# 2. Suggest an edit to fix the above code.
def func_1():
    colors = ['red', 'green', 'blue', 'purple']
    for i in range(len(colors)):
        try:
            print(colors[5])
        except IndexError as err:
            print(err)


# 3. What is the main risk with the code below: file does not exist
# 4. How would you protect the above code? And why? try except
def func_2():
    try:
        my_file = open('C://test//README.txt').read()
        print(my_file)
    except IOError as err:
        print(err)


# 5. Write a program which will:
# A. Create a folder named “test” (anywhere on your computer)
# B. Create a file named “name” containing your name inside.
def func_3():
    if not os.path.exists('test'):
        os.mkdir('test')
    if not os.path.exists('test/name'):
        file = open('test/name', 'w+')
        file.write('nir')
        file.close()


# 6.
# A. Install python-docx python library through CMD /Terminal:
# B. Create a docx file using the documentation:
# https://python-docx.readthedocs.io/en/latest/user/documents.html
# Write your name inside the docx file
def func_4():
    document = Document()
    document.add_paragraph('Nir')
    document.save('test.docx')


def main():
    # func_1()
    # func_2()
    # func_3()
    func_4()


if __name__ == "__main__":
    main()
