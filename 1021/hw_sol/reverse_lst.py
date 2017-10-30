def reverse_lst(lst):
	reversed_lst = []
	for i in range(len(lst) - 1, -1, -1):
		reversed_lst.append(lst[i])

	return reversed_lst


input_lst = [12, 'a', 3434, '000']
print(reverse_lst(input_lst))
