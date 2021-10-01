h = int(input())
count = 0
for i in range(h + 1):
	for j in range(60):
		for k in range(60):
		    # 매시각안에'3'이포함되어있다면카운트증가
		    if '3' in str(i) + str(j) + str(k):
			    count += 1
print(count)
