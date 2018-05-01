
def insertionSort(arr):
#iterating through elements
	for i in range(len(arr)):
		pos=i
		element=arr[i]
		while pos>0 and element<arr[pos-1]:
			arr[pos]=arr[pos-1]
			pos=pos-1
		arr[pos]=element
	return arr

arr=insertionSort([5,2,3,11,8,7,0,1,9,36])
print ("Insertion Sort array is:")
for j in arr:
	print(j)

	
	
