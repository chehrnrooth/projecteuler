#@author chehrnrooth
def triplet():
	'''
	Input: Nothing
	Output:sum, a, b, c and abc
	'''
	a, b, c = 1, 1, 1
	for c in range(1, 1000):
		for b in range(1, c):
			for a in range(1, b):	
				sum = a+b+c
				if sum == 1000 and a**2 + b**2 == c**2:
					print sum, a, b, c
					triple = a*b*c
					return triple
print triplet()



