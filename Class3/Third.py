import sys


def func_1():
    file_txt = 'c:/DevOps/DevOpsExperts/Class3/1.txt'
    file = open(file_txt, 'r', encoding='utf-8')
    print(file.read())
    file.close()

    file = open(file_txt, 'a', encoding='utf-8')
    file.write(' fuchs')
    file.close()

    file = open(file_txt, 'r', encoding='utf-8')
    print(file.read())
    file.close()


def func_2():
    file_txt = 'c:/DevOps/DevOpsExperts/Class3/1.txt'
    file = None
    try:
        file = open(file_txt)
        print(file.read())
    except IOError as err:
        print(err)
    finally:
        print(123)
        if file != None:
            file.close()


def func_3():
    x = 7
    y = 4
    x += 6
    x = 9
    print(x)
    print(y)


def main():
    # func_1()
    # func_2()
    func_3()


if __name__ == "__main__":
    main()
