#author chehrnrooth answer: 4613732
def fib(maximum):
	a, b = 0, 1
	count = 0
	while a < maximum:
		a, b = b, a+b
		if b%2 == 0:
			count+=b
	return count
maximum = 4000000
print 'The sum of the even fibonacci numbers under', maximum, 'is', fib(maximum)
