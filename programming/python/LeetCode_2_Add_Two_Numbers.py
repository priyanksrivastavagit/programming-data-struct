# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        resListNode = ListNode(val = (l1.val + l2.val) % 10)
        carryValue = (l1.val + l2.val) // 10
        currentNode = resListNode

        while l1.next and l2.next:
            l1 = l1.next
            l2 = l2.next
            currentNode.next = ListNode(val = (l1.val + l2.val + carryValue) % 10)
            carryValue = (l1.val + l2.val + carryValue) // 10
            currentNode = currentNode.next

        while l1.next:
            l1 = l1.next
            currentNode.next = ListNode(val = (l1.val + carryValue) % 10)
            carryValue = (l1.val + carryValue) // 10
            currentNode = currentNode.next

        while l2.next:
            l2 = l2.next
            currentNode.next = ListNode(val = (l2.val + carryValue) % 10)
            carryValue = (l2.val + carryValue) // 10
            currentNode = currentNode.next

        if carryValue > 0:
            currentNode.next = ListNode(val = 1)

        return resListNode

