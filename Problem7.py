#@author chehrnrooth
def prime(x):
	'''
	Input: integer above 0
	Output: Prime number corresponding to the number inputted
	Time for 10001: 260.1 seconds
	'''
	count = 1
	for num in range(2, 110000):
		for i in range (2, num):
			if num%i==0:
				break
		else:
			print num, count
			if count == x:
				return num, count
			count +=1
x = int(input('What number prime do you want to find?: '))
print prime(x)

