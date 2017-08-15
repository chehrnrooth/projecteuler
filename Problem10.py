#@author chehrnrooth
def prime(x):
  '''
  Input: Int for max prime
  Output: prime, sum at that time, return sum overall
  '''
	count = 0
	for x in range(2, x):
		for i in range (2, y):
			if x%i == 0:
				break
		else:
			print x, count
			count+=x
	return count
print prime(2000000)
