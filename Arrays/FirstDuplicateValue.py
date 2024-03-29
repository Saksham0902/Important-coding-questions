# Given an array of integers between 1 and n , inclusive, where n is the length of tm
# array, write a function that returns the first integer that appears more than once (whet
# the array is read from left to right).
# In other words, out of all the integers that might occur more than once in the input
# array, your function should return the one whose first duplicate value has the
# minimum index.
# If no integer appears more than once, your function should return -1 .
# Note that you're allowed to mutate the input array.
# Sample input1:
# array = [2, 1, 5, 2, 3, 3, 4]
# Sample output1:
# 2
#
# Sample input2:
# array = [2, 1, 5, 3, 3, 2, 4]
# Sample output2:
# 3


def firstDuplicateValue(array):
    # Write your code here.
    for value in array :
		if array[abs(value) - 1] < 0:
			return abs(value)
		array[abs(value)-1] *= -1
	return -1
