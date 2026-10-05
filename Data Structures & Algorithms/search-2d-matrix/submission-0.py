class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        ri, rf = 0, len(matrix)-1
        mid = 0
        while ri <= rf:
            mid = (ri + rf )//2 
            if matrix[mid][0] > target:
                rf = mid - 1
            elif matrix[mid][-1] < target:
                ri = mid + 1
            else:
                break
            
        
        ci, cf = 0, len(matrix[mid])-1
        
        while ci <= cf:
            mid2 = (ci+cf)//2
            if matrix[mid][mid2] > target:
                cf = mid2 - 1
            elif matrix[mid][mid2] < target:
                ci = mid2 + 1
            else:
                return True
        
        return False