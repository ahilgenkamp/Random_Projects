# fizbuzz test

def fizzbuzz(start, end):
	fizzbuzz = []
	for i in range(start,end):
		if i % 3 == 0 and i % 5 == 0:
			fizzbuzz.append('fizzbuzz')
		elif i % 3 == 0:
			fizzbuzz.append('fizz')
		elif i % 5 == 0:
			fizzbuzz.append('buzz')
		else:
			fizzbuzz.append(str(i))
	return fizzbuzz

print(fizzbuzz(1,101))


def fizzbuzz2(start, end):
	fizzbuzz = []
	for i in range(start,end):
		output = ''
		if i % 3 == 0: output += 'fizz'
		if i % 5 == 0: output += 'buzz'

		if output == '':
			fizzbuzz.append(str(i))
		else:
			fizzbuzz.append(output)
	return fizzbuzz

print(fizzbuzz2(1,101))