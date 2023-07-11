"""
File: boggle.py
Name: Zoe
----------------------------------------
TODO: build a letter_matrix game "Boggle". Find the English words inside.
"""

import time
import re

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'

dictionary = []  # construct dictionary  # 自己加的


def main():
	"""
	TODO:
	"""
	start = time.time()
	####################
	# Define the regular expression pattern
	pattern = r'^[a-zA-Z]{1} [a-zA-Z]{1} [a-zA-Z]{1} [a-zA-Z]{1}$'  # ^: from start, {1}: one letter, $: to the end
	letter_matrix = []  # construct a list to store letters in 4 rows
	for i in range(1, 5):
		row = input(f"{i} row of letters: ")
		if not re.match(pattern, row):  # check if match the pattern
			print("Illegal input")
		else:
			letter_matrix.append(row.lower().split())  # case insensitive and store each row in letter_matrix`/ split: split str to list

	# Read the dictionary
	read_dictionary()

	# create a 4*4 matrix list contains False
	selected_matrix = [[False for _ in range(4)] for _ in range(4)]
	# DON'T USE: selected_matrix = [[False] * 4] * 4
	# any modification made to one row will be reflected in all the rows.

	# create a list to store found words
	found_words = []

	# choose a first letter and search the word
	for row in range(0, 4):
		for col in range(0, 4):
			letter = letter_matrix[row][col]  # randomly choose a first letter
			selected_matrix[row][col] = True  # set this first letter to True
			search_words(letter_matrix, selected_matrix, letter, found_words, row, col)
			selected_matrix[row][col] = False  # return to default state, and start with another first letter

	# print the number of found words
	print(f'There are {len(found_words)} words in total.')
	####################
	end = time.time()
	print('----------------------------------')
	print(f'The speed of your boggle algorithm: {end - start} seconds.')


def search_words(letter_matrix, selected_matrix, word, found_words, row, col):
	"""
	This function search the possible words of a letter located at row and col
	"""
	if has_prefix(word) is True:
		# check if the word is a valid word
		if len(word) >= 4 and word in dictionary and word not in found_words:
			print(f"Found \"{word}\"")
			found_words.append(word)

		# get the neighbors
		neighbors = get_neighbors(row, col)

		# check each neighbor
		for neighbor in neighbors:
			n_row, n_col = neighbor
			if not selected_matrix[n_row][n_col]: # check the state is False
				selected_matrix[n_row][n_col] = True  # set to True, preventing from being selected again in the search
				search_words(letter_matrix, selected_matrix, word + letter_matrix[n_row][n_col], found_words, n_row,
							 n_col)
				selected_matrix[n_row][n_col] = False  # after the search, turn the state into default False


def get_neighbors(row, col):
	"""
	This function find the neighbors positions of a letter located at row and col
	:param row: original row
	:param col: original column
	:return: a list of positions of neighbors
	"""
	neighbors = []
	for i in range(-1, 2):
		for j in range(-1, 2):
			n_row = row + i  # n_row: neighbor row
			n_col = col + j  # n_col: neighbor column
			if 0 <= n_row < 4 and 0 <= n_col < 4 and (i != 0 or j != 0):  # check within the box & not original position
				neighbors.append((n_row, n_col))  # store neighbor's position
	return neighbors


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	with open(FILE) as file:
		for dict_word in file.readlines():
			dictionary.append(dict_word.strip())
	# return dictionary    # not necessary


def has_prefix(sub_s):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	# iterate through the dictionary
	for word in dictionary:
		if word.startswith(sub_s):
			return True  # if word start with sub_s
	return False  # if word doesn't start with sub_s


if __name__ == '__main__':
	main()
