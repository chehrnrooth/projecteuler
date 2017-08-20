def trianglenum(num):
	'''
	Input: Triangle # in the sequence
	Output: triangle number up to a certain point
	'''
	count = 0
	while num > 0:
		count += num
		num-=1
	num = count
	return num

def divisorcheck(num):
	'''
	Input: Int(triangle number)
	Output: Int and # of divisors (should be 100)
	'''
	count = 0
	for x in range(1, num):
		if num%x == 0:
			count+=1
			#print num, 'Divisor:', x
			#no else, restricts it to only finding one divisor
	return count
#Checks for a certain number of divisors
maxrange = 1000
x = 1
while x <= maxrange:
	print divisorcheck(trianglenum(x)), trianglenum(x), x
	if divisorcheck(trianglenum(x)) >= 500:
		print divisorcheck(trianglenum(x)), trianglenum(x)
	x+=1
