# Write a function that takes in an array of at least three integers and, without sorting the
# input array, returns a sorted array of the three largest integers in the input array.
# The function should return duplicate integers if necessary; for example, it should return
# [10,10,12] for an input array of [10, 5, 9,10, 12] .

# Sample Input:
# array = [141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]
# Sample Output:
# [18, 141, 541]

def findThreeLargestNumbers(array):
    # Write your code here.
    l = []
	l.extend(array[0:3])
	j = 3
	fun(array,l,j)
	l[0],l[2]=l[2],l[0]
	return l

def fun(array,l,j):


	if l[0] >= l[1] and l[0]>=l[2]:
		if l[2]>l[1]:
			l[1],l[2] = l[2],l[1]
	elif l[1]>=l[2] and l[1]>=l[0]:
		l[0],l[1] = l[1],l[0]
		if l[2]>l[1]:
			l[2],l[1]= l[1],l[2]
	elif l[2]>= l[0] and l[2]>=l[1]:
		l[2],l[0] = l[0],l[2]
		if l[2]>l[1]:
			l[1],l[2] = l[2],l[1]

	for i in range(j,len(array)):
		if array[i]>l[2]:
			l[2]=array[i]

			fun(array,l,i+1)
			break
