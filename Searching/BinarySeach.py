# Sample Input :
# array = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]
# target = 33
# Sample Output:
# 3



def binarySearch(array, target):
    # Write your code here.
    return binarySearchHelper(array,target,0,len(array)-1)

def binarySearchHelper(array,target,left,right):
	if left >right:
		return -1
	middle = (left + right)//2
	tnumber = array[middle]
	if target < tnumber:
		return binarySearchHelper(array,target,left,middle-1)
	elif target > tnumber:
		return binarySearchHelper(array,target,middle+1,right)
	else:
		return middle
