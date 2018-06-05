
def BubbleSort(al):
    
    swap=True
    while swap:
        swap=False
        for i in range(len(al)-1):
            if(al[i]>al[i+1]):
                al[i],al[i+1] =al[i+1],al[i]
                swap=True  
    return al
	
arrayList=[1,2,3,4,5,6,67,787,34,67867,786754,56]
print(BubbleSort(arrayList))
	
	

	
	
