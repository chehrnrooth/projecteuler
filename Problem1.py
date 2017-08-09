#author chehrnrooth answer: 234168
count = 0
num = 0
while num <=1000:
	if num%5 == 0 and num%3 == 0:
		count += num
	elif num%5 == 0 or num%3==0:
		count += num
	num +=1
print (count)
