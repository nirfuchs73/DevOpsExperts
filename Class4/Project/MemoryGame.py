
import random
import time
import Utils


# generate a sequence of random numbers (between 1 to 101) in the size of difficulty
# show the sequence for 0.7 seconds
# return the sequence
def generate_sequence(difficulty):
    nums = []
    for i in range(difficulty):
        nums.insert(i, random.randint(1, 101))
    print(nums)
    time.sleep(0.7)
    Utils.screen_cleaner()
    return nums


# get a sequence of numbers from the user and return the sequence
def get_list_from_user(difficulty):
    print('After seeing the numbers enter the numbers you saw, each one separated with Enter.')
    nums = []
    for i in range(difficulty):
        num = int(input())
        nums.insert(i, num)

    return nums


# compare list_a to list_b. if list are equal return True, else return False
def is_list_equal(list_a, list_b):
    for item in list_a:
        if not item in list_b:
            return False
    return True


# play game - return True (user win) or False (user lose)
def play(difficulty):
    random_list = generate_sequence(difficulty)
    user_list = get_list_from_user(difficulty)
    return is_list_equal(random_list, user_list)
