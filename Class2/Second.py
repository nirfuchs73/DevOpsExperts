# import datetime
import array as array
from datetime import datetime
# for x in range(10):
#     print(x)
#     if x == 7:
#         break

# for x in range(10):
#     if x == 3:
#         continue
#     print(x)

# for x in range(2, 10):
#     print(x)

# for x in range(3, 8, 2):
#     print(x)

# x = 1
# while x < 6:
#     print(x)
#     x += 1


def func():
    return 4


def func1(num):
    print(num)


def func2(num):
    return num + 2


def add(num1, num2):
    return num1 + num2


name = 'nir'


def func3():
    global name
    name = 'nir1'
    print(name)


# a = arr.array('i', [1, 2, 3])
# a[0] = 2
# print(a[0])
# a.append(7)
# print(a)


def main():
    print('this is main')
    # print(datetime.now())
    # arr = [1, 2, 3]
    # arr = array.array('i', [1, 2, 3])
    # arr[0] = 2
    # print(arr[0])
    # arr.append(7)
    # print(arr[3])
    # arr.pop(0)
    # print(arr[0])
    # arr.insert(1, 8)
    # print(arr[1])
    # print(len(arr))

    # print(arr)
    # for num in arr:
    #     print(num)
    # for i in range(len(arr)):
    #     print(arr[i])

    # lst = [4, 5, 6]
    # lst[0] = 44
    # print(lst[0])
    # lst.append(7)
    # print(lst[3])
    # lst.pop(0)
    # print(lst[0])
    # lst.insert(0, 8)
    # print(lst[0])

    # print(lst)

    # tuple
    # seasons = ('summer', 'winter', 'spring', 'fall')
    # # print(seasons[0])
    # for season in seasons:
    #     print(season)

    # dictionary
    dict = {'a': 1, 'b': 2, 'c': 3, 'a': 4}
    print(dict)
    print(dict['b'])
    dict['a'] = 11
    print(dict['a'])
    del(dict['a'])

    print(dict.keys())
    print(dict.values())
    # print(dict)


if __name__ == "__main__":
    main()
    # print(func())
    # func1(7)
    # print(func2(4))
    # print(add(2, 7))
    # print(add('1111', '2222'))
    # func3()
