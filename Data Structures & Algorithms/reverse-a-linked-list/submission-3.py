# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head
        
        dummy = ListNode(-1)
        curr = head
        while curr != None:
            next_node = curr.next
            curr.next = dummy.next
            dummy.next = curr
            
            curr = next_node
        
        return dummy.next