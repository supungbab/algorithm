input_data = input()

row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1

#나이트가이동할수있는8가지방향정의
steps = [(-2,-1),(-1,-2),(1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1)]
#8가지방향에대하여각위치로이동이가능한지확인
result=0
for step in steps:
	#이동하고자하는위치확인
	next_row=row+step[0]
	next_column=column+step[1]
	#해당위치로이동이가능하다면카운트증가
	if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
		result+=1
print(result)
