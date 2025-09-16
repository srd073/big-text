data = []
count = 0
with open('reviews.txt','r') as f:
	for line in f:
		data.append(line)
		count += 1
		if (count % 10000) == 0:
			print(count)
print('檔案讀取完成,總共有',count,'筆資料！')	
print(data[0])
print('=====================')
# print(data[1])

dlen = 0
for d in data:
	dlen += len(d)

print('留言的平均長度為：',dlen / len(data))	
