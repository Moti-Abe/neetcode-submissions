# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        arr = []
        for i in range(len(lists)):
            curr = lists[i] 
            while curr:
                arr.append(curr.val)
                curr = curr.next

        arr.sort()
        dummy = ListNode()
        curr = dummy
        for i in range(len(arr)):
            temp = ListNode(arr[i])
            curr.next = temp
            curr = curr.next
        return dummy.next

            
        