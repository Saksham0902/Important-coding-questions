# Write a function that takes in a Binary Search Tree (BST) and a target integer value and
# returns the closest value to that target value contained in the BST.
# You can assume that there will only be one closest value.
# Each BST node has an integer value , a left child node, anda right child
# node. A node is said to be a valid BST node if and only if it satisfies the BST property:
# its value is strictly greater than the values of every node to its left; its value is less
# than or equal to the values of every node to its right; and its children nodes are either
# valid BST nodes themselves or None / null .

def findClosestValueInBst(tree, target):
    # Write your code here.
    return findClosestValueInBstHelper(tree,target,tree.value)
def findClosestValueInBstHelper(tree,target,closest):
	if tree is None:
		return closest
	while tree is not None:
		if abs(target - closest) > abs(target - tree.value):
			closest = tree.value
		if target > tree.value:
			tree = tree.right
		elif target < tree.value:
			tree = tree.left
		else:
			break
	return closest



# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# def findClosestValueInBst(tree, target):
#     # Write your code here.
# 	return findClosestValueInBstHelper(tree,target,tree.value)
#
# def findClosestValueInBstHelper(tree,target,closest):
# 	if tree is None:
# 		return closest
# 	if abs(target-closest)>abs(target - tree.value):
# 		closest = tree.value
# 	if target <tree.value:
# 		return findClosestValueInBstHelper(tree.left,target,closest)
# 	elif target >tree.value:
# 		return findClosestValueInBstHelper(tree.right,target,closest)
# 	else:
# 		return closest
#
#
#
# # This is the class of the input tree. Do not edit.
# class BST:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None
