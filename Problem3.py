#author chehrnrooth answer: 6857
def func(n):
	''' 
	Finding the largest prime factor of a number
	'''
	i = 2
	while i*i<n:
		while n%i==0:
			n=n/i
		i+=1
	return n
print func(600851475143)
