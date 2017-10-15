"""
7. list 연습2

list 내 최대값을 갖는 원소가 몇 개인지 구해보세요.
lst = [2, 3, 6, 2, -1, 0, 6, 2, 3] 이 주어져 있을 때, 최대값인 6은 2개 있습니다.
여기서 6의 개수인 2를 출력해 보세요.
이 때 다음과 같은 포맷으로 출력해 보세요: 'max = 6, num_max = 2'.

"""

lst = [2, 3, 6, 2, -1, 0, 6, 2, 3]
max_val = max(lst)
num_max = 0

for e in lst:
	# If e is the maximum element
	if e == max_val:
		num_max += 1

print(num_max)

