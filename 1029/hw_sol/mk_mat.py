"""
1. 파일 입력 연습
어떤 텍스트 파일을 읽어 matrix로 리턴해주는 함수를 만들어보세요.
텍스트파일 예제로는 mat1.txt 과 mat2.txt 가 주어집니다.

예)
mat1.txt가
1 2 3 5
3 5 2 1
5 3 1 5
이면, [[1, 2, 3, 5], [3, 5, 2, 1], [5, 3, 1, 5]] 인 리스트를 리턴해 보세요.

힌트) 아래와 같은 skeleton code 를 사용할 수 있습니다.

def read_matrix(filename):
	# Read the file
	f = ???

	# Get the file contents
	contents = ???

	# Parse the contents and make it in a matrix form
	???

	# Return the matrix
	???

"""

def read_matrix(filename):
	# Read the file
	f = open(filename, 'r')

	# Get the file contents
	contents = f.readlines()

	# Close the file
	f.close()

	# Parse the contents and make it in a matrix form
	for th, line in enumerate(contents):
		element_lst = line.split()
		contents[th] = element_lst

	# Return the matrix
	return contents


mat1 = read_matrix('../mat1.txt')
print(mat1)

mat2 = read_matrix('../mat2.txt')
print(mat2)
