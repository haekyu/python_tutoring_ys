"""
6. list 연습1

list 내 최대값 구하기. 
lst = [2, 3, 6, 2, -1, 0, 6, 2, 3] 이 주어져 있을 때 최대값인 6을 출력해보세요.

힌트1) 간단하게 max(lst) 로도 구할 수 있지만, max()를 쓰지 않고 loop로 해결해 보세요.
힌트2) skeleton code를 이용해도 좋습니다. ??? 을 채워 넣으면 됩니다.

"""

# Target list
lst = [2, 3, 6, 2, -1, 0, 6, 2, 3]

# Initialize max_val
max_val = -999

# Get the maximum value in lst
for e in lst:
	# Get the temporal max_val
	if max_val < e:
		# max_val is no longer the maximum value
		# e should be the new maximum value
		max_val = e

print(max_val)

