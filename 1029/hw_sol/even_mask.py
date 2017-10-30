def even_mask(lst):
	result = []
	for e in lst:
		result.append(e % 2 == 0)

	return result


def even_mask2(lst):
	return [(e % 2 == 0) for e in lst]


input_lst = [3, 2, 6, 1, 2, 0]
print(even_mask(input_lst))
print(even_mask2(input_lst))

