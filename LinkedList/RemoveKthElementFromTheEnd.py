# Sample Input :
# head = 0->1->2->3->4->5->6->7->8->9
# k=4
# Sample Output:
# 0->1->2->3->4->5->7->8->9

class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeKthNodeFromEnd(head, k):
    # Write your code here.
    node = head

	count = 0
	while node is not None:
		count += 1
		node = node.next

	front = count - k
	count = 0
	nodet = head
	if count == front:
		head.value = head.next.value
		head.next = head.next.next
		return head

	while count!= front:
		count+=1
		if count ==front :
			break
		nodet = nodet.next

	nodet.next = nodet.next.next
	return nodet
