"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
2. 함수 연습 2
rank 구하기.
학생들의 점수를 input으로 받고, 각 학생들의 등수를 return하는 함수를 만들어 보세요. 
학생들의 점수는 숫자로 된 리스트가 들어옵니다.
점수가 높으면 등수는 높아집니다.
등수는 1등부터 시작합니다.

예) input이 scores = [3, 4, 5, 1, 2] 이면
0번째 학생: 점수=3, 등수=3등
1번째 학생: 점수=4, 등수=2등
2번째 학생: 점수=5, 등수=1등
3번째 학생: 점수=1, 등수=5등
4번째 학생: 점수=2, 등수=4등
이므로, 등수를 순서대로 뽑은 리스트인 [3, 2, 1, 5, 4] 를 return하면 됩니다.

힌트) 학생 A의 등수는 "자신(A)의 점수보다 높은 다른 사람들의 명 수 + 1" 이 됩니다.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def rank(scores):
	rank_lst = []
	for my_th, my_score in enumerate(scores):
		# Count the number of other people 
		#  whose score is biggger than my score
		num_better = 0

		for other_th, other_score in enumerate(scores):
			# Skip myself
			if my_th == other_th:
				continue

			if my_score < other_score:
				num_better = num_better + 1

		# Save my rank
		my_rank = num_better + 1
		rank_lst.append(my_rank)

	return rank_lst


input_scores = [3, 4, 5, 1, 2]
output_ranks = rank(input_scores)
print(output_ranks)

