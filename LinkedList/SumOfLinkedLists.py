# Sample Input :
# linkedListOne = 2->4->7->1
# linkedListTwo = 9->4->5
# Sample Output :
# 1->9->2->2(1742+549)

class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def sumOfLinkedLists(linkedListOne, linkedListTwo):
    # Write your code here.
    nodeOne = linkedListOne
	nodeTwo = linkedListTwo
	valueOne = 0
	valueTwo = 0
	count = 10
	i = 0
	while nodeOne is not None :
		valueOne += (nodeOne.value)*(count**i)
		i+=1
		nodeOne = nodeOne.next
	i = 0
	while nodeTwo is not None :
		valueTwo += (nodeTwo.value)*(count**i)
		i+=1
		nodeTwo = nodeTwo.next
	sume = valueOne + valueTwo
	tlist= dummy = LinkedList(0)
	for i in reversed(str(sume)):
		tlist.next = LinkedList(int(i))
		tlist = tlist.next
		if tlist is None:
			break
	return dummy.next
