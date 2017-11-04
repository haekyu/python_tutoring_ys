"""
3. Bubble sort를 구현해 보세요.
어떤 list가 주어져있을 때, sorted list가 output이면 됩니다.
"""

def bubble_sort(lst):
	for round_th in range(len(lst)):
		for left_idx in range(0, len(lst) - round_th - 1):
			# If the window has a contracting order
			if lst[left_idx] > lst[left_idx + 1]:
				# Swap
				lst_left = lst[left_idx]
				lst[left_idx] = lst[left_idx + 1]
				lst[left_idx + 1] = lst_left
	return lst


lst = [3, 2, 1, 4, 6, 2, 3, 0, -1, 3, 4, 5, 2]
sorted_lst = bubble_sort(lst)
print(sorted_lst)
