"""
File: anagram.py
Name: HJ
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time                   # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop

# Global Variable
d = {}


def main():
    """
    The program searches and prints each anagrams for the word input by user
    """
    start = time.time()
    ####################
    print(f'Welcome to stanCode "Anagram Generator" (or {EXIT} to quit)')
    while True:
        anagram = input('Find anagrams for: ')
        if anagram == EXIT:
            break
        else:
            anagram = anagram.lower()
            print(f'Searching...')
            read_dictionary(anagram)
            find_anagrams(anagram)
    ####################
    end = time.time()
    print('----------------------------------')
    print(f'The speed of your anagram algorithm: {end-start} seconds.')


def read_dictionary(s):
    """
    :param s: str, the word input by user
    """
    global d
    with open(FILE, 'r') as f:
        for line in f:
            if len(line.strip()) == len(s):
                d[line.strip()] = len(line.strip())


def find_anagrams(s):
    """
    :param s: str, the word input by user
    call the helper function and print the total number of anagrams and anagrams themselves
    """
    count_lst = []
    anagrams_lst = []
    find_anagrams_helper(s, [], count_lst, anagrams_lst)
    print(f'{sum(count_lst)} anagrams: {anagrams_lst}')


def find_anagrams_helper(s, current_l, count_lst, anagrams_lst):
    """
    :param s: str, the word input bt user
    :param current_l: lst, for character permutation
    :param count_lst: lst, count the number of anagrams
    :param anagrams_lst: lst, record the anagrams
    """
    global d
    if len(s) == 0:
        current_s = ''
        for ch in current_l:
            current_s += ch
        if current_s in d and current_s not in anagrams_lst:  # for identical ch in a word, the same permutation occurs
            print(f'Found: {current_s}')
            print('searching...')
            anagrams_lst.append(current_s)
            count_lst.append(1)
    elif len(current_l) == 2:     # for early stopping
        sub_s = ''
        for ch in current_l:
            sub_s += ch
        if has_prefix(sub_s):
            for i in range(len(s)):
                current_l.append(s[i])
                s_lst = []
                for ch in s:
                    s_lst.append(ch)
                s_lst.pop(i)
                new_s = ''
                for ch in s_lst:
                    new_s += ch
                find_anagrams_helper(new_s, current_l, count_lst, anagrams_lst)
                current_l.pop()
    else:
        for i in range(len(s)):
            # choose
            current_l.append(s[i])
            s_lst = []  # make 's' a list to pop the ch which has been appended to current_l
            for ch in s:
                s_lst.append(ch)
            s_lst.pop(i)
            new_s = ''   # convert s_lst to a new string for next recursion to use
            for ch in s_lst:
                new_s += ch
            # explore
            find_anagrams_helper(new_s, current_l, count_lst, anagrams_lst)
            # un-choose
            current_l.pop()


def has_prefix(sub_s):
    """
    :param sub_s: str, consists of a few characters to search prefix in d
    :return: boolean, True if word in d has prefix of sub_s
                      False if no such prefix exists in d
    """
    global d
    for key in d:
        if key.startswith(sub_s):
            return True
    return False


if __name__ == '__main__':
    main()
