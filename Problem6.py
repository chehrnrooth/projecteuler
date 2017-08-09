#author chehrnrooth answer: 25164150
maxrange, count, count2 = 100, 0, 0
for x in xrange(maxrange+1):
	count += x
	if count > 5000:
		count = count**2
for x in xrange(maxrange+1):
	y = x**2
	count2 += y
	if count2 > 330000:
		total = count - count2
		print 'The answer is', total
