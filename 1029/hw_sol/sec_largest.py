def get_second_largest(lst):
	fst_max, sec_max = 0, 0
	for e in lst:
		# If e is the fst max
		if fst_max < e:
			sec_max = fst_max
			fst_max = e
		# If e is the sec max
		elif sec_max < e:
			sec_max = e

	return sec_max


input_lst = [3, 2, 2, 0, 2, 1, 1]
print(get_second_largest(input_lst))

