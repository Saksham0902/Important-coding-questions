



def nodeDepths(root):
    # Write your code here.
    sums = []
	calculateNodeDepths(root,0,sums)
	return sum(sums)
def calculateNodeDepths(node,depthsum,sums):
	if node is None:
		return
	totalDepth = depthsum +1
	sums.append(totalDepth-1)
	if node.left is None and node.right is None:

		return
	calculateNodeDepths(node.left,totalDepth,sums)
	calculateNodeDepths(node.right,totalDepth,sums)


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
