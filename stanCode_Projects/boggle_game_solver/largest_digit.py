"""
File: largest_digit.py
Name: HJ
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""


def main():
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
	"""
	:param n: int, a number
	:return: helper function
	"""
	return helper(n, 0)


def helper(n, largest_digit):
	"""
	:param n: int, a number
	:param largest_digit: int,
	:return: int, the largest digit
	"""
	if n == 0:   # base case
		return largest_digit
	else:
		if n < 0:   # convert negative n into positive if any
			n = n * -1
		if n % 10 > largest_digit:
			largest_digit = n % 10
		return helper(int(n/10), largest_digit)  # round down the value of n/10


if __name__ == '__main__':
	main()
