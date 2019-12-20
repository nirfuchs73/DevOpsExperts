import random


# return random number from 1 - difficulty
def generate_number(difficulty):
    return random.randint(1, difficulty)


# return guess from user
def get_guess_from_user(difficulty):
    return int(input('Guess a number between 1 to {}:'.format(difficulty)))


# compare random number to user guess
def compare_results(difficulty, secret_number):
    if difficulty == secret_number:
        return True
    else:
        return False


# play game - return True (user win) or False (user lose)
def play(difficulty):
    secret_number = generate_number(difficulty)
    # print('secret_number', secret_number)
    guess_from_user = get_guess_from_user(difficulty)
    return compare_results(guess_from_user, secret_number)
