def findElement (arr, n) :
	leftMax = [0] * n

	leftMax[0] = -99999
	for i in range(1,n) :
		if leftMax[i-1] > arr[i-1] :
			leftMax[i] = leftMax[i-1]
		else :
			leftMax[i] = arr[i-1]
			
	rightMin = 99999
	for i in range(n-1,-1,-1) :
		if leftMax[i] < arr[i] and rightMin > arr[i] :
			return i
		if rightMin > arr[i] :
			rightMin = arr[i]
			
	return -1

arr = [5,1,4,3,6,8,10,7,9]
n = len(arr)

idx = findElement(arr,n)
print(idx)
