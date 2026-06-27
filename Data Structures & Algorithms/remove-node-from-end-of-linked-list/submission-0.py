# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        arr = []
        curr = head
        while curr:
            arr.append(curr.val)
            curr = curr.next
        del arr[len(arr) - n]

        if(len(arr) == 0):
            return None
        
        curr = head
        for i in range(len(arr)):
            curr.val = arr[i]
            if i == len(arr)-1:
                break
            curr = curr.next
        curr.next = None


        return head

