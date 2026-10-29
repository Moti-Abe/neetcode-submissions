# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        curr = dummy
        arr1 = []
        arr2 = []
        while l1 and l2:
            arr1.append(str(l1.val))
            arr2.append(str(l2.val))
            l1 = l1.next
            l2 = l2.next
        while l1:
            arr1.append(str(l1.val))
            l1 = l1.next
        while l2:
            arr2.append(str(l2.val))
            l2 = l2.next
        arr1.reverse()
        arr2.reverse()
        s1 = "".join(arr1)
        s2 = "".join(arr2)
        res = int(s1) + int(s2)
        res = str(res)
        res = list(res)
        res.reverse()
        for i in range(len(res)):
            node = ListNode(int(res[i]))
            curr.next = node
            curr = curr.next

        return dummy.next

