"""
2. 파일 출력 연습
어떠한 리스트를 csv (comma-separated values) 포맷으로 텍스트파일에 저장해보세요.

예)
[[1, 2, 3, 5], [3, 5, 2, 1], [5, 3, 1, 5]]
라는 리스트가 주어져 있으면
1,2,3,5
3,5,2,1
5,3,1,5
로 텍스트파일(파일 이름 맘대로)에 저장해 보세요.
"""

def save_mat_csv(filename, mat):
	f = open(filename, 'w')
	for rows in mat:
		for th, element in enumerate(rows):
			f.write("%s" % element)
			if th < len(rows) - 1:
				f.write(",")
		f.write("\n")


mat = [[1, 2, 3, 5], [3, 5, 2, 1], [5, 3, 1, 5]]
save_mat_csv('./result_csv.txt', mat)
