class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        arr = []
        curr = head

        # Store linked list values in an array
        while curr:
            arr.append(curr.val)
            curr = curr.next

        temp = []
        count = 0
        arr1 = []

        # Divide the array into groups of k
        for i in range(len(arr)):
            arr1.append(arr[i])
            count += 1

            if count == k:
                temp.append(arr1)
                arr1 = []
                count = 0

        # Reverse each complete group
        for i in range(len(temp)):
            temp[i].reverse()

        # Reconstruct the array
        result = []
        for group in temp:
            result.extend(group)

        # Add remaining elements without reversing
        result.extend(arr1)

        # Reconstruct the linked list
        dummy = ListNode(0)
        curr = dummy

        for val in result:
            curr.next = ListNode(val)
            curr = curr.next

        return dummy.next