"""
File: boggle.py
Name: HJ
----------------------------------------
This program finds words at least four letters long form 4 x 4 grid of letters,
following the sequences of adjacent letters which are horizontally, vertically, and diagonally neighboring,
and each grid of the letter can only be used once per word.
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'


def main():
	"""
	input 4 rows of 4 letters, the program prints words at least 4 letters long by connecting letters through one of
	their neighbors (upper, upper-right, right, lower-right, lower, lower-left, left, or upper-left letter)
	then neighbor's one of its neighbors and so on so forth, without repeating the same neighbor in a word.
	"""
	start = time.time()
	####################
	boggle = []
	for i in range(4):
		row = input(f'{i+1} row of letter: ')
		if row[0].isalpha() and row[1] == ' ' and row[2].isalpha() and row[3] == ' ' and row[4].isalpha() \
			and row[5] == ' ' and row[6].isalpha():
			row = row.lower()   # case insensitive
			letters = []  # make each row a list
			for ch in row:
				if ch.isalpha():
					letters.append(ch)
			boggle.append(letters)  # put 4 lists of the row in a list
		else:
			break   # illegal format
	if len(boggle) != 4:
		print('Illegal format')
	else:
		find_words(boggle)
	####################
	end = time.time()
	print('----------------------------------')
	print(f'The speed of your boggle algorithm: {end - start} seconds.')


def find_words(boggle):
	"""
	:param boggle:lst, storing 4 row-of-letters lists
	"""
	pass_record = []
	for i in range(len(boggle)):
		pass_record.append([0, 0, 0, 0])
	word_lst = []
	chosen = ''
	# loop letter one by one
	for i in range(len(boggle)):
		for j in range(len(boggle[0])):
			chosen += boggle[i][j]
			pass_record[i][j] = 1
			find_words_helper(boggle, i, j, chosen, pass_record, word_lst)
			chosen = chosen[:-1]
			pass_record[i][j] = 0
	print(f'There are {len(word_lst)} words in total.')


def find_words_helper(boggle, i, j, chosen, pass_record, word_lst):
	"""
	:param boggle: lst, storing 4 row-of-letters lists
	:param i: int, letter's x position index
	:param j: int, letter's y position index
	:param chosen: str, a letter from boggle
	:param pass_record: lst, storing 0 if not passed yet
	:param word_lst: lst, storing words
	"""
	# Base Case
	if len(chosen) >= 4 and chosen in read_dictionary(chosen) and chosen not in word_lst:
		print(f'Found "{chosen}"')
		word_lst.append(chosen)
		# keep searching for longer letters of the word
		for x in range(i-1, i+2):
			for y in range(j-1, j+2):
				if 0 <= x < 4 and 0 <= y < 4:
					if x != i or y != j:
						if pass_record[x][y] == 0:
							chosen += boggle[x][y]
							if has_prefix(chosen):
								pass_record[x][y] = 1
								find_words_helper(boggle, x, y, chosen, pass_record, word_lst)
								pass_record[x][y] = 0
							chosen = chosen[:-1]
	# find the letter's neighbor
	else:
		for x in range(i-1, i+2):
			for y in range(j-1, j+2):
				if 0 <= x < 4 and 0 <= y < 4:
					if x != i or y != j:   # exclude the letter itself
						if pass_record[x][y] == 0:  # exclude passed letter
							# Choose
							chosen += boggle[x][y]
							if has_prefix(chosen):
								pass_record[x][y] = 1
								# Explore
								find_words_helper(boggle, x, y, chosen, pass_record, word_lst)
								# Un-choose
								pass_record[x][y] = 0
							chosen = chosen[:-1]


def read_dictionary(word):
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	# d = {}
	# with open(FILE, 'r') as f:
	# 	for line in f:
	# 		line = line.strip()
	# 		if len(word) >= 4:
	# 			if len(line) == len(word) and line[0] == word[0] and line[1] == word[1]:
	# 				d[line] = len(line)
	# 		else:
	# 			if len(line) >= 4 and line[0] == word[0] and line[1] == word[1]:
	# 				d[line] = len(line)
	# return d
	d = []
	with open(FILE, 'r') as f:
		for line in f:
			line = line.strip()
			if len(word) >= 4:
				if len(line) == len(word) and line[0] == word[0] and line[1] == word[1] and line[2] == word[2]:
					d.append(line)
			else:  # for sub_s
				if len(line) >= 4 and line[0] == word[0] and line[1] == word[1]:
					d.append(line)
	return d


def has_prefix(sub_s):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	if len(sub_s) == 1:
		return True
	else:
		for wd in read_dictionary(sub_s):
			if wd.startswith(sub_s):
				return True
	return False


if __name__ == '__main__':
	main()
