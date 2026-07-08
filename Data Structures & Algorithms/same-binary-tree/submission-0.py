# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        p_arr = []
        q_arr = []

        def inorder_p(p):
            if not p:
                p_arr.append("None")
                return 
            p_arr.append(p.val)
            inorder_p(p.left)
            
            inorder_p(p.right)
        
        def inorder_q(q):
            if not q:
                q_arr.append("None")
                return
            q_arr.append(q.val)
            inorder_q(q.left)
            
            inorder_q(q.right)
        
        inorder_p(p)
        inorder_q(q)
    
        if len(p_arr) != len(q_arr):
            return False
        for i in range(len(p_arr)):
            if p_arr[i] != q_arr[i]:
                return False
        return True
        
            


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna