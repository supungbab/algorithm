def reorder(arr, n):
	j = 0 # Count of non-zero elements
	for i in range(n):
		if arr[i] != 0:
		# here count is incremented
			arr[j] = arr[i]
			j+=1
	for i in range(j, n):
		arr[i] = 0
# code
arr = [6, 0, 8, 2, 3, 0, 4, 0, 1]
n = len(arr)
reorder(arr, n)
print(arr)
