
"""
File: anagram.py
Name: Zoe
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
import time  # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'  # This is the filename of an English dictionary
EXIT = '-1'  # Controls when to stop the loop

dictionary = []  # construct dictionary


def main():
    read_dictionary()
    s = input('Welcome to stanCode \'\'Anagram Generator\'\' (or -1 to quit)\nFind anagrams for:')
    start = time.time()
    while True:
        if s != EXIT:
            anagrams_lst = find_anagrams(s)
            print(f'{len(anagrams_lst)} anagrams: {anagrams_lst}')
            s = input('Find anagrams for:')
        else:
            break
    end = time.time()
    print('----------------------------------')
    print(f'The speed of your anagram algorithm: {end - start} seconds.')


def read_dictionary():
    with open(FILE) as file:
        for word in file.readlines():
            dictionary.append(word.strip())


def find_anagrams(s):
    """
    :param s:
    :return:
    """
    anagrams_lst = []  # construct anagrams list
    find_anagrams_helper('', s, anagrams_lst)
    return anagrams_lst


def find_anagrams_helper(current, remaining, anagrams):
    if len(remaining) == 0:
        # check if in dictionary and prevent duplication in anagrams_lst
        if current in dictionary and current not in anagrams:
            print(f'Found: {current}')
            anagrams.append(current)   # add current to  anagrams list
            print('Searching...')

    else:
        for i in range(len(remaining)):
            # choose
            char = remaining[i]
            new_current = current + char    # notes: no need to un-choose, unless using current += char
            if has_prefix(new_current) is True:
                new_remaining = remaining[:i] + remaining[i + 1:]
                # explore
                find_anagrams_helper(new_current, new_remaining, anagrams)


def has_prefix(sub_s):
    """
    :param sub_s:
    :return:
    """
    # iterate through the dictionary
    for word in dictionary:
        if word.startswith(sub_s):
            return True         # if word start with sub_s
    return False                # if word doesn't start with sub_s


if __name__ == '__main__':
    main()
