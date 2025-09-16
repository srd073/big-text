data=[]
count=0
with open('reviews.txt',r) as f
	while line in f:
		data.append(line)
		count += 1

print(count)		