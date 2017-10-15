color_dict = dict() 
color_dict["abc"] = "red"
color_dict["abcd"] = "blue"
color_dict["a"] = "dark-blue"
color_dict["ab"] = "yellow"
color_dict["b"] = "pink"
color_dict["c"] = "red"

color_dict["abc"]
"abc" in color_dict


"""
lst1 = [2, 2, 0, 1, 0]
lst2 = [333, 2, 1, 0, 0]
lst3 = ['a', 'b', 'c', 'd', 0]

# for i in range(len(lst1)):
# 	print("index is ", i)
# 	print(lst1[i], lst2[i], lst3[i])

# for i, e in enumerate(lst1):
# 	print(lst1[i], lst2[i], lst3[i])	

for (e1, e2, e3) in zip(lst1, lst2, lst3):
	print(e1, e2, e3)


# 함수 f(x) = x + 1
def f1(x):
	y = x + 1
	return y

def f2(x):
	return x + 1


# 함수 g(x, y) = x + y
def g(x, y):
	return x + y
"""
"""
함수를 구현할 건데, 그 함수의 이름은 h
파라미터는 x, y, z 가 있고
y, z는 default parameter이고, z, y를 3으로 이니셜 셋팅

리턴 값은 x * y * z



함수 cal_max를 만들거예요
parameter는 어떤 리스트
그 리스트의 최댓값을 리턴


1~n 중에서 소수 프린트하는 함수
근데, 1~100까지 뽑는 게 디폴트이길 원해요.
"""


"""
lst = [1, 2, 3, 3, 2, 1]
max_val = max(lst)

idx = 0
want_idx = 0
for e in lst:
	if e == max_val:
		want_idx = idx
	idx += 1			

print(want_idx)


print("max_val=", max_val)


print("max_val=%d" % max_val)


while i <= 10:
	if i <= 5:
		^
	else:
		v

max(lst)


for i in range(1, 101):
	# flag (True/False, 0, 1, 2, 3)
	is_i_prime = True

	for j in range(2, i):
		// 만약 i가 j로 나누어 떨어지면
		if (i % j == 0):
			is_i_prime = False
			break

	if is_i_prime:
		print(i)
"""