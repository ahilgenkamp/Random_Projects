

def cutSticks(lengths):
	# Write your code here
	len_sort = sorted(lengths, key = lambda x: x)
	num_sticks - [len(len_sort)]
	list_len = len(len_sort)
	while list_len > 1:
		short = len_sort[0]
		for i in len_sort:
			if i <= short:
				len_sort = len_sort[1:]
			else:
				pass
		len_sort = [x - short for x in len_sort]
		num_sticks.append(len(len_sort))
		list_len = len(len_sort)
	return num_sticks


def isPossible(a, b, c, d):
	# Write your code here
	if a == c and b == d:
		return 'Yes'
	elif a < c:
		return isPossible((a+b),b,c,d)
	elif b < d:
		return isPossible(a,(a+b),c,d)
	else:
		return 'No'