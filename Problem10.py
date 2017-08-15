#@author chehrnrooth, with help from the internet.
sieve = [True]*2000000 #creates a sieve of 2 million
def mark(sieve, x):
	'''
	takes a prime, finds its multiples and deletes them from the sieve. 
	'''
	for i in xrange(x+x, len(sieve), x): #skips around with step x
		sieve[i] = False
for x in xrange(2, int(len(sieve)**0.5)+1):
	if sieve[x]: 
		mark(sieve, x) #call to def
print sum(i for i in xrange(2, len(sieve)) if sieve[i])
