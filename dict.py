#讀取大檔案,計算共有幾筆留言
data = []
count = 0
with open('reviews.txt','r') as f:
	for line in f:
		data.append(line)
		count += 1
		if (count % 10000) == 0:
			print(count)
print('檔案讀取完成,總共有',count,'筆資料！')	
#print(data[0])
print('=====================')
# print(data[1])
#----------------------------------------

#計算留言的平均長度
dlen = 0
for d in data:
	dlen += len(d)

print('留言的平均長度為：',dlen / len(data))	 
#----------------------------------------

#獲取留言長度小於100
new=[]
for d in data:
	if len(d)<100 :
		new.append(d)
print('一共有',len(new),'筆留言長度小於100')		
print(new[0])
#print(new[1])
#----------------------------------------

#留言內容有good字樣時,則存入good[]的list之中
good=[]
for d in data:
	if 'good' in d:
		good.append(d)
print('一共有',len(good),'筆留言提到good')
# 以上四行快寫法:good = [d          for d in data if 'good' in d]
#              good = [1          for d in data if 'good' in d]
#              good = ['bad' in d for d in data if 'good' in d]		
print(good[0])

bad=[]
for d in data:
	bad.append('bad' in d)
print(bad)	
#------------------------------------------

#dict 字典
# list 與 dict 區別 :
#     list = []                        # list 用法
#     dict = { key:value,key:value }   # dict 用法

# 統計所有的字分別放入dict
wc= {}
for d in data:
	words=d.split()
	for word in words:
		if word in wc:
			wc[word] += 1
		else:
			wc[word] = 1	

for word in wc:
	if wc[word] > 1000000:   #百萬以上
		print(word,wc[word])

print(len(wc))		
print(wc['Allen'])

while True:
	word=input('請問你想查什麼字：(q離開)')
	if word == 'q':
		break
	if word in wc:
		print(word,'出現過的次數為：',wc[word])
	else:
		print('這個字沒有出現過喔！')

print('感謝使用本查詢功能！')				
