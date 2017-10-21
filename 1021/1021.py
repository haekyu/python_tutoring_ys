print("당신이 좋아하는 숫자를 입력하세요:")
your_favorite = input()

print("당신이 좋아하는 숫자는?", your_favorite)

def count(lst, pivot):
	i = 0
	for e in lst:
		if e > pivot:
			i = i + 1
	return (i)

def rank(input_lst):
	rank_lst = []
	for j in input_lst:
		print('-' * 10)
		print('before append', rank_lst)
		rank_lst.append(count(input_lst, j) + 1)
		print('after append', rank_lst)
	return rank_lst


# **** the input (== input_lst) should be exist **** #
input_lst = [1, 2, 3]
toss_receiver_rank_lst = rank(input_lst)
print(toss_receiver_rank_lst)
