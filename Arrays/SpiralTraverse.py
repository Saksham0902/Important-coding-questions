# Write a function that takes in an n x m two-dimensional array (that can be square-
# shaped when n == m) and returns a one-dimensional array of all the array's elements in
# spiral order.
# Spiral order starts at the top left corner of the two-dimensional array, goes to the right,
# and proceeds in a spiral pattern all the way until every element has been visited.
#
# Sample Input :
# array = [[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]]
#
# Sample Output:
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]


def spiralTraverse(array):
    # Write your code here.
	result=[]
	startrow,endrow = 0, len(array)-1
	startcolumn,endcolumn = 0 , len(array[0]) -1

	while startrow <= endrow and startcolumn <=endcolumn :
		for col in range(startcolumn , endcolumn +1):
			result.append(array[startrow][col])
    	for row in range(startrow+1,endrow+1):
			result.append(array[row][endcolumn])
		for col in reversed(range(startcolumn,endcolumn)):
			if startrow == endrow:
				break
			result.append(array[endrow][col])
		for row in reversed(range(startrow+1,endrow)):
			if startcolumn == endcolumn:
				break
			result.append(array[row][startcolumn])

		startrow += 1
		endrow -=1
		startcolumn += 1
		endcolumn -=1
	return result
