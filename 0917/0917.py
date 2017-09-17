# 2, 4, 6, 8, 10
i = 1
test_iter = 0
while i <= 10000000:
	if test_iter > 3:
		test_iter = test_iter + 1
		break
	if (i % 2 == 0):
		if i == 6:
			i = i + 1
			continue
		print(i)
	# else:
	# 	print('여기는 홀수구나')
	i = i + 1

# if i가 짝수:
# 	ㄴㅇㄹㄴㅇㄹ
# elif i가 홀수:
# 	ㄴㄹㅇㄴㄹㄴㅇㄹ
# ******* else: ******
# 	sdfsfsdfsd
# 	print('ERR!!!!!!! 여기는 금지구역이야')
	
# range
# for i in ???????:
# 	print(i)


# while 문 예제
"""
i = 0
while (i < 10):
	print('small i=%d' % i)
	i = i + 2
"""
# s = 'a'
# while (len(s) < 3):
# 	print(s)
# 	s = s + 'a'

# for

# print(0)
# print(1)
# print(2)
# for i in range(5, 12, 3):
# 	print(i)


# for i in [2, 4, 6, 8, 10]:
# 	print(i)

# for i in [2, 'abc', 6, [3, 3, 3], 10]:
# 	print(i)

'''
i = 1
if (i > 10):
	print('hello big')
else:
	print('small')
'''
# i = 10
# # i를 3으로 나눈 몫
# # hint: %, / 사용
# r = i % 3
# int(3.0) == 3
# int(2.3) == 2
# int(2.9) == 2
# int(-3.2) == -3

# i = -9
# # Q1
# if (not(i 가 10 이하이면 and i 가 0보다 크)):
# 	print(i)
# 그렇지 않으면:
# 	print(i + 1)

# # Q2
# if (i - 10 이 0 이상이면):
# 	print(i)
# 그렇지 않으면:
# 	print(i + 1)
