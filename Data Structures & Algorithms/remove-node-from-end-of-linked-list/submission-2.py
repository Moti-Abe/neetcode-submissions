# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        total_len = 0
        curr = head 
        
        while curr != None:
            total_len += 1
            curr = curr.next

        if total_len == 1:
            return head.next
            

        removed = total_len - n
        if removed == 0:
            head = head.next
        curr = head
        count = 0
        while curr != None:
            count += 1
            if count == removed:
                curr.next = curr.next.next
                break
            curr = curr.next
        
        return head

