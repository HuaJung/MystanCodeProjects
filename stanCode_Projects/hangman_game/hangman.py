"""
File: hangman.py
Name: HJ
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    This program prints the following messages to tell users
    1) What the random word looks like which is presented in dashes as per its length at first
    2) the guesses are left, one less at a time if guessing wrongly, or no changes if guessing correctly
    3) inputting ane character at a time
    repeat over until users achieve the whole letter or use up guesses, and it prints out the answer.
    """
    answer = random_word()
    left_guesses = N_TURNS  # assign the number of guesses to a new box
    dashed = dashed_word(answer)
    drawing(left_guesses)
    print('The word looks like: ' + dashed)
    print('You have ' + str(left_guesses) + ' guesses left.')
    hanging_process(answer, dashed, left_guesses)
    print('The word was: ' + answer)


def drawing(left_guesses):
    for i in range(8):
        print('=', end='')
    print('')
    if left_guesses == N_TURNS:
        for i in range(6):
            print('|')
    elif left_guesses == N_TURNS - 1:
        print('|    |')
        for i in range(5):
            print('|')
    elif left_guesses == N_TURNS - 2:
        print('|    |')
        print('|   ( )')
        for i in range(4):
            print('|')
    elif left_guesses == N_TURNS - 3:
        print('|    |')
        print('|   ( )')
        print('|    #')
        print('|    #')
        for i in range(3):
            print('|')
    elif left_guesses == N_TURNS - 4:
        print('|    |')
        print('|   ( )')
        print('|  ~ # ~')
        print('|    #')
        for i in range(2):
            print('|')
    elif left_guesses == 2:
        print('|    |')
        print('|   ( )')
        print('|  ~ # ~')
        print('|    #')
        print('|   / \\')
        for i in range(1):
            print('|')
    elif left_guesses == 1:
        print('|    |')
        print('|  (0.0)')
        print('|  ~ # ~')
        print('|    #')
        print('|   / \\')
        for i in range(1):
            print('|')
    else:
        print('|    |')
        print('|   (X)')
        print('|  ~ # ~')
        print('|    #')
        print('|   / \\')
        print('|   Lose')


def hanging_process(answer, dashed, left_guesses):
    """
    :param answer: str, from random_word
    :param dashed: str, the number of '-' as per the length of answer
    :param left_guesses: int, the number of guesses at the beginning
    :return: print he updated dashed, left_guesses, and win or lose messages
    """
    while True:
        input_ch = input('Your guess: ')
        if not input_ch.isalpha() or len(input_ch) > 1:
            # the input_ch might be a digit or more than one character'
            print('illegal format')
        else:
            input_ch = input_ch.upper()
            # the input_ch is one character and case-insensitive
            if input_ch in answer:
                # if you guess right
                ans = ""
                for i in range(len(answer)):
                    ch1 = answer[i]
                    ch2 = dashed[i]
                    # answer and dashed share the same length / index
                    if ch1 == input_ch:
                        ans += input_ch
                        # add input_ch into ans where it in answer
                    else:
                        ans += ch2
                        # add dashed into ans where it used to be
                dashed = ans
                print('You are correct!')
                drawing(left_guesses)
                if dashed == answer:
                    print('You win!!')
                    break
            else:
                left_guesses -= 1
                print('There is no ' + input_ch + "'s in the word.")
                drawing(left_guesses)
                if left_guesses == 0:
                    print('You are completely hung : (')
                    break
            print('The word looks like: ' + dashed)
            print('You have ' + str(left_guesses) + ' guesses left.')


def dashed_word(answer):
    """
    :param answer: str, from random_word
    :return: str, the number of '-' as per the length of answer
    """
    ans = ""
    for i in answer:
        ans += '-'
    return ans


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
