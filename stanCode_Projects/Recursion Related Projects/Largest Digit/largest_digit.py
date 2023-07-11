"""
File: largest_digit.py
Name: Zoe
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""
k = 0


def main():
	# global k    # see the bigO
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9
	# print('run times: ', k)


def find_largest_digit(n):
	"""
	:param n:
	:return:
	"""
	# global k    # see the bigO
	# k += 1
	# convert negative integer to positive
	if n < 0:
		n *= -1

	# units digits
	if n < 10:
		return n

	# get units digit
	units_digit = n % 10
	# get remaining number (after removing the units digit)
	rest_number = n // 10
	# recursion
	rest_largest_digit = find_largest_digit(rest_number)

	# compare units_digit and rest_largest_digit
	if units_digit > rest_largest_digit:
		return units_digit
	else:
		return rest_largest_digit


if __name__ == '__main__':
	main()
