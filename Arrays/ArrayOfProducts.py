# Write a function that takes in a non-empty array of integers and returns an array of the
# same length, where each element in the output array is equal to the product of every
# other number in the input array.
# In other words, the value at output [i] is equal to the product of every number in
# the input array other than input[i]
# Note that you're expected to solve this problem without using division.
# Sample Input
# array : [5, 1, 4, 2]
# Sample Output
# [8, 40, 10, 20]
# 8 is equal to 1 x 4 x 2
# 40 is equal to 5 x 4 x 2
# 10 is equal to 5 x 1 x 2
# 20 is equal to 5 x 1 x 4


def arrayOfProducts(array):
    # Write your code here.
	l=[]

	c=1

	if array.count(0) ==1:
		a = array.index(0)
		l.extend(array)
		l.remove(l[a])
		print(l)
		for i in range(len(l)):
			c = c*l[i]
		print(c)
		l.clear()
		l.extend([0]*len(array))
		l[a] = c


	else:
		for i in range(len(array)):
			c =c*array[i]
		l.extend([c]*(len(array)))
		for i in range(len(array)):
			if array[i] == 0:
				l[i]=0
			else:
				l[i] = l[i]/array[i]

	return l
