"""
8. list 연습3

list 내 최대값을 갖는 원소의 index를 구해보세요.
lst = [2, 3, 6, 2, -1, 0, 6, 2, 3] 이 주어져 있을 때, 
최대값인 6의 index는 2, 6 입니다. 둘 중 하나를 출력해 보세요.
"""
import numpy as np
lst = [2, 3, 6, 2, -1, 0, 6, 2, 3]
idx_of_max_element = np.argmax(lst)
print(idx_of_max_element)
