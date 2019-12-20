import Utils
import MemoryGame
import GuessGame
import Score


# print welcome message
def welcome(name):
    print('Hello', name, 'and welcome to the World of Games (WoG).')
    print('Here you can find many cool games to play.')


def load_game():
    # let the user choose game and difficulty.
    print('Please choose a game to play:')
    print('1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back')
    print('2. Guess Game - guess a number and see if you chose like the computer')
    game = int(input())
    difficulty = int(input('Please choose game difficulty from 1 to 5:'))

    win = False
    if game < 1 or game > 2 or difficulty < 1 or difficulty > 5:  # invalid choice
        print(Utils.ERROR_MESSAGE)
        load_game()
    elif game == 1:  # play Memory Game
        win = MemoryGame.play(difficulty)
    else:  # play Guess Game
        win = GuessGame.play(difficulty)

    # print(win)
    if win:  # if user win update score
        print('You win additional', difficulty, 'points')
        Score.add_score(difficulty)
    else:  # if user lose load game
        print('Try again')
        load_game()
