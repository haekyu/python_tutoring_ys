"""
5. loop문 연습5

소수(prime number) 출력하기.
1부터 100까지의 수 중에서 소수인 것들을 출력해 보세요.
예를들어,
2
3
5
...
89
97
을 출력해 보세요.

힌트1) 어떤 자연수 n이 소수인지 판단하려면 간단하게 'n보다 작은 수 중에서 n을 
나누어 떨어지게 하는 것이 있는지 없는지' 를 보면 됩니다.

"""

def print_primes(n):
	for i in range(2, n + 1):
		# Declare a flag
		is_i_prime = True

		# Check if i is a prime number
		for j in range(2, i):
			# if i has a factor
			if i % j == 0:
				is_i_prime = False
				break

		# Print the result
		if is_i_prime:
			print(i)

print_primes(100)
