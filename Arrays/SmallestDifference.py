# Write a function that takes in two non-empty arrays of integers, finds the pair of
# numbers (one from each array) whose absolute difference is closest to zero, and
# returns an array containing these two numbers, with the number from the first array in
# the first position.
# Note that the absolute difference of two integers is the distance between them on the
# real number line. For example, the absolute difference of -5 and 5 is 10, and the
# absolute difference of -5 and -4 is 1.
# You can assume that there will only be one pair of numbers with the smallest
# difference.
# Sample Input:
# arrayOne :[-1, 5, 10, 20, 28, 3]
# arrayTwo : [26, 134, 135, 15, 17]
# Sample Output:
# [28, 26]



def smallestDifference(arrayOne, arrayTwo):
    # Write your code here.
    arrayOne.sort()
	arrayTwo.sort()
	idxOne = 0
	idxTwo = 0
	smallest = float("inf")
	current = float("inf")
	smallestPair = []
	while idxOne < len(arrayOne) and idxTwo < len(arrayTwo):
		firstNum = arrayOne[idxOne]
		secondNum = arrayTwo[idxTwo]
		if firstNum < secondNum:
			current = secondNum - firstNum
			idxOne+=1
		elif secondNum < firstNum:
			current = firstNum - secondNum
			idxTwo+=1
		else:
			return([firstNum,secondNum])
		if current < smallest:
			smallest = current
			smallestPair = [firstNum,secondNum]
	return(smallestPair)
