# You're given an array of integers and another array of three distinct integers. The first
# array is guaranteed to only contain integers that are in the second array, and the
# second array represents a desired order for the integers in the first array. For example,
# a second array of [x, y, z] represents a desired order of
# [x,x,,,,,,,,x,y,y,y,y,,,,,y,z,z,z] in the first array.
# Write a function that sorts the first array according to the desired order in the second
# array.
# The function should perform this in place (i.e., it should mutate the input array), and it
# shouldn't use any auxiliary space (i.e., it should run with constant space: 0(1) space).
# Note that the desired order won't necessarily be ascending or descending and that the
# first array won't necessarily contain all three integers found in the second array—it
# might only contain one or two.

# Sample Input:
# array = [1, 0, 0, -1, -1, 0, 1, 1]
# order = [0, 1, -1]
# Sample Output:
# [0, 0, 0, 1, 1, 1, -1, -1]


def threeNumberSort(array, order):
    # Write your code here.
    firstValue = order[0]
	secondValue = order[1]

	firstIdx,secondIdx , thirdIdx = 0,0,len(array)-1

	while secondIdx<=thirdIdx:
		value = array[secondIdx]
		if value == firstValue:
			array[secondIdx],array[firstIdx] = array[firstIdx],array[secondIdx]
			firstIdx +=1
			secondIdx +=1
		elif value == secondValue:
			secondIdx +=1
		else:
			array[secondIdx],array[thirdIdx] = array[thirdIdx],array[secondIdx]
			thirdIdx -=1
	return array

    # def threeNumberSort(array, order):
    # # Write your code here.
    # firstValue = order[0]
	# secondValue = order[1]
    #
	# firstIdx = 0
	# for i in range(len(array)):
	# 	if array[i] ==firstValue:
	# 		array[firstIdx],array[i] = array[i],array[firstIdx]
	# 		firstIdx+=1
	# for i in range(firstIdx,len(array)):
	# 	if array[i] ==secondValue:
	# 		array[firstIdx],array[i] = array[i],array[firstIdx]
	# 		firstIdx+=1
	# return array
# def threeNumberSort(array, order):
#     # Write your code here.
# 	valueCounts = [0,0,0]
#
# 	for ele in array:
# 		orderIdx = order.index(ele)
# 		valueCounts[orderIdx] +=1
#
# 	for i in range(3):
# 		count = valueCounts[i]
# 		value = order[i]
#
# 		elebefore = sum(valueCounts[:i])
# 		for n in range(count):
# 			currentIdx = n + elebefore
# 			array[currentIdx] = value
#
# 	return array
