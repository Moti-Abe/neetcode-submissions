class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        # Previous smallest element
        pse = [-1]*n 
        pse_stack = deque()
        for i in range (n):
            while pse_stack and heights[pse_stack[-1]] >= heights[i]:
                pse_stack.pop()
            if pse_stack:
                pse[i] = pse_stack[-1]
            pse_stack.append(i)
        
        
        # Next smallest element
        nse = [n]*n
        nse_stack = []
        for i in range (n-1, -1, -1):
            while nse_stack and heights[nse_stack[-1]] >= heights[i]:
                nse_stack.pop()
            if  nse_stack:
                nse[i] = nse_stack[-1]
            nse_stack.append(i)
        
        # Calculate max area using nse and pse
        max_area = 0
        for i in range(n):
            width = nse[i] - pse[i] - 1
            area = heights[i]* width
            max_area = max(max_area, area )
        return max_area