# Sol 1
def gen_lst_1():
	return [i for i in range(1, 6)]

# Sol 2
def gen_lst_2():
	lst = [0] * 5
	for i in range(1, 6):
		lst[i - 1] = i
	return lst


if __name__ == '__main__':
	lst = gen_lst_2()
	print(lst)
