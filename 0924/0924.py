# numpy를 사용하고 싶으면
import numpy

mat1 = numpy.array([[1, 2], [3, 4], [5, 6]])
mat2 = mat1.T  # transpose
print(mat2)
print(mat1)
mat3 = numpy.dot(mat1, mat2)  # matrix multiplication
vec1 = numpy.array([2, 3, 4])
mat5 = numpy.matmul(mat2, vec1)
print(mat5)
print(mat3)
print(mat1[1])
print(mat1[:, 1])
print(mat1[1][1])
print(mat1[1, 1])  # 정석
# mat[row][col]
# : --> 전체



arr = numpy.array([-1, 2, 3])
print(arr)

print(numpy.average(arr))

x = -234
x = numpy.abs(x)
print(x)

new_arr = numpy.absolute(arr)
print(new_arr)



# print(sdfsdfsdf)

'''
# 1. int로 바꿔보고 --> 만약 음수면 양수로 바꿔주고 --> len()
if x < 0:
	x = x * -1

# 형 변환
	- int(3.222) == 3
	- int("343")
'''

# * --> regular expression

# cnt_a = 0
# for s in ['a', 'b', 'c']:
# 	if s == 'a':
# 		cnt_a = cnt_a + 1
'''
if ("an" in i) == True:

if ("an" in i):
'''

# for i in [1, 2, 3]:
# 	print(i)

# x = 1

# if x < 10:
# 	x = x + 1
# else:
# 	x = x - 1
# 	x = 10

# # str = 3

# str(3)
# == 3(3)
