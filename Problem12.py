def trianglenum(num):
	'''
	Input: Triangle # in the sequence
	Output: even triangle numbers up to the maxrange
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
			#no else, restricts it to only finding one divisor
	return count
#Checks for a certain number of divisors
x = 1
while True:
	if trianglenum(x)%10==0:
		print divisorcheck(trianglenum(x)), trianglenum(x), x
		if divisorcheck(trianglenum(x)) >= 500:
			print divisorcheck(trianglenum(x)), trianglenum(x), x
			break
	x+=1
