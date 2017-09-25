def avglst(lst):
	sum_element = 0
	num_element = 0
	for element in lst:
		sum_element += element
		num_element += 1
	avg = sum_element / num_element
	return avg


if __name__ == '__main__':
	test = [-923, 0, 1, 3, 23, 4324]
	avg = avglst(test)
	print(avg)

