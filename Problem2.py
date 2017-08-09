#author chehrnrooth answer: 4613732
a, b = 0, 1
maximum = 4000000
count = 0
while a < 4000000:
	a, b = b, a+b
	if b%2 == 0:
		count+=b
print('This is the sum of the fibonacci number',count)
