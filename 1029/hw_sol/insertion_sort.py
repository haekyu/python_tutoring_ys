"""
4. Insertion sort를 구현해 보세요.
어떤 list가 주어져있을 때, sorted list가 output이면 됩니다.
"""

def insertion_sort(lst):
	for round_th in range(len(lst) - 1):
		# Insert new_idx-th element
		new_idx = round_th + 1

		# Find out the right position to insert the new_idx-th element
		i = 0
		is_new_largest = 1
		for i in range(0, round_th + 1):
			if lst[new_idx] < lst[i]:
				is_new_largest = 0
				break

		# If the new value is not largest
		if not is_new_largest:
			# Get the new value to be inserted
			val_of_new = lst[new_idx]

			# Move the bigger values right one step 
			lst[i + 1: round_th + 2] = lst[i: round_th + 1]

			# Insert the new value
			lst[i] = val_of_new

	return lst

lst = [3, 2, 1, 4, 6, 2, 3, 0, -1, 3, 4, 5, 2]
sorted_lst = insertion_sort(lst)
print(sorted_lst)

