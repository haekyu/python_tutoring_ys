
# call by value
def change_val(a):
	a = a + 2

b = 10
change_val(b)
print(b)
print("-" * 10)

# call by reference
def add_value(d):
	d["b"] = ["bear"]

c = {"a": ["apple", "aurora"]}

print('Before', c)
add_value(c)
print('After', c)

print("-" * 10)

for i in range(3, 1, -1):
	print(i)



def larger_cnt(lll, i):
	j = 0
	for e2 in lll:
		if e2 > i:
			j = j + 1
	return j


def second_third_largest(lst):
	for e in lst:

		j = 0
		for e2 in lst:
			if e2 > e:
				j = j + 1

		lar_cnt = j

		# lar_cnt = larger_cnt(lst, e)


		if lar_cnt == 1:
			result = e

	return (result)


