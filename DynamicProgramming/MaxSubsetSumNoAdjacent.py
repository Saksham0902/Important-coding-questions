# Write a function that takes in an array of positive integers and returns the maximum
# sum of non-adjacent elements in the array.
# If the input array is empty, the function should return 0 .
Sample Input:
array = [75, 105, 120, 75, 90, 135]
Sample Output:
330

def maxSubsetSumNoAdjacent(array):
    # Write your code here.
    if not len(array):
		return 0
	elif len(array) == 1:
		return array[0]

	second = array[0]
	first = max(array[0],array[1])
	for i in range(2,len(array)):
		current = max(first,second+array[i])
		second = first
		first = current

	return first



# def maxSubsetSumNoAdjacent(array):
#     # Write your code here.
#     if not len(array) :
# 		return 0
# 	elif len(array)==1:
# 		return array[0]
# 	else:
# 		maxSums = array[:]
# 		maxSums[1] = max(array[0],array[1])
# 		for i in range(2,len(array)):
# 			maxSums[i] = max(maxSums[i-1],maxSums[i-2] + array[i])
# 		return maxSums[-1]
