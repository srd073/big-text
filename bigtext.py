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

new=[]
for d in data:
	if len(d)<100 :
		new.append(d)

print('一共有',len(new),'筆留言長度小於100')		
print(new[0])
print(new[1])

good=[]
for d in data:
	if 'good' in d:
		good.append(d)
print(good[0])








