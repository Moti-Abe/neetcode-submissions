# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        arr = []
        curr = head

        while curr:
            arr.append(curr.val)
            curr = curr.next

        curr = head
        l, r = 0, len(arr) - 1

        while l < r:
            curr.val = arr[l]
            curr = curr.next

            curr.val = arr[r]
            curr = curr.next

            l += 1
            r -= 1

        if curr:
            curr.val = arr[l]