# Write a function that takes in a non-empty array of distinct integers and an integer
# representing a target sum. The function should find all quadruplets in the array that
# sum up to the target sum and return a two-dimensional array of all these quadruplets
# in no particular order.
# If no four numbers sum up to the target sum, the function should return an empty
# array.
# Sample input:
# array =[7, 6, 4, -1, 1, 2]
# Sample output:
# [[7, 6, 4, -1], [7, 6, 1, 2]] (the quadruplets could be ordered differently)

def fourNumberSum(array, targetSum):
    # Write your code here.
    allpairsum = {}
	quadruplets = []
	for i in range(1, len(array)-1):
		for j in range(i+1,len(array)):
			currentsum = array[i] + array[j]
			difference = targetSum - currentsum
			if difference in allpairsum:
				for pair in allpairsum[difference]:
					quadruplets.append(pair + [array[i], array[j]])
		for k in range(0,i):
			currentsum = array[i] + array[k]
			if currentsum not in allpairsum:
				allpairsum[currentsum] = [[array[k],array[i]]]
			else:
				allpairsum[currentsum].append([array[k],array[i]])
	return quadruplets
