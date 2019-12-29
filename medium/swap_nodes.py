# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return str(self.val)

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return
        print(head)
        second = ListNode(head.val)
        first = ListNode(head.next.val)
        first.next = second
        recursed = self.swapPairs(head.next.next)
        first.next.next = recursed
        
        return first

def build_nodes(nodes):
    node = ListNode(nodes[0])
    for i in range(1,len(nodes)):
        print(i)
        node.next = ListNode(nodes[i])

    return node

if __name__ == "__main__":
    # node = build_nodes([1,2,3,4])
    # for _ in range(len([1,2,3,4])):
    #     print(node)
    #     node = node.next
    pass