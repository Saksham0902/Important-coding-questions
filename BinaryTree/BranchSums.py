# Write a function that takes in a Binary Tree and returns a list of its branch sums
# ordered from leftmost branch sum to rightmost branch sum.
# A branch sum is the sum of all values in a Binary Tree branch. A Binary Tree branch is a
# path of nodes in a tree that starts at the root node and ends at any leaf node.
# Each BinaryTree node has an integer value , a left child node, anda ri ght
# child node. Children nodes can either be BinaryTree nodes themselves or None /
# null .

class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
    # Write your code here.
	sums = []
	calculateBranchSums(root,0,sums)
	return sums

def calculateBranchSums(node,runningSum,sums):
	if node is None:
		return
	newRunningSum = node.value + runningSum
	if node.left is None and node.right is None:
		sums.append(newRunningSum)
		return
	calculateBranchSums(node.left,newRunningSum,sums)
	calculateBranchSums(node.right,newRunningSum,sums)
