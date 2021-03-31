# Sample Input:
# [1, 2, 3]
# Sample Output:
# [[],[1],[2],[1, 2],[3],[1, 3],[2, 3],[1, 2, 3]]





def powerset(array):
    # Write your code here.
    subsets = [[]]
	for i in array:
		for j in range(len(subsets)):
			current = subsets[j]
			subsets.append(current+[i])
	return subsets


# def powerset(array,idx = None):
#     # Write your code here.
#
#     if idx is None:
# 		idx = len(array) - 1
# 	if idx<0:
# 		return [[]]
# 	ele = array[idx]
# 	subsets = powerset(array,idx-1)
# 	for i in range(len(subsets)):
# 		current = subsets[i]
# 		subsets.append(current+[ele])
# 	return subsets
