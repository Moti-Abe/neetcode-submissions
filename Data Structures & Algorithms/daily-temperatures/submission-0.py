class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        st = deque()
        n = len(temperatures)
        nge = [0]*n
        st.append((temperatures[-1], n-1))

        for i in range(n-2,-1,-1):
            
            while st and temperatures[i] >= st[-1][0]:
                st.pop()
            if not st:
                st.append((temperatures[i], i))
            if st and temperatures[i] < st[-1][0]:
                nge[i] = st[-1][1]
                st.append((temperatures[i], i))
        
        for i in range(n):
            if nge[i] == 0:
                continue
            nge[i] = nge[i]-i
        
        return nge
            
            
                
                


