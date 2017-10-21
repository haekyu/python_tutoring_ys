"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
3. 함수 연습 3
시작하는 알파벳 구하는 함수 구현하기.
어떤 string이 input으로 주어져있을 때, 그 input의 가장 앞 알파벳을 출력하는 함수를 만들어 보세요.

예) input이 "apple" 이면 "a" 를 return.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def get_initial_char(input_str):
	return input_str[0]

first_of_apple = get_initial_char("apple")
print(first_of_apple)


