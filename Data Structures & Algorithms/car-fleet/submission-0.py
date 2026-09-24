class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        st = deque()
        pos_speed = []
        n = len(speed)
        pos_speed = []

        for i in range(n):
            pos_speed.append([position[i], speed[i]])
        
        pos_speed.sort(key=lambda x: x[0])

        for i in range(n-1,-1,-1):
            t = (target - pos_speed[i][0])/pos_speed[i][1]
            if st and t <= st[-1]:
                continue
            st.append(t)
        
        return len(st)




        