class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r = len(matrix)-1
        l = m = 0
        while l <= r:
            m = l +((r-l)//2)
            if matrix[m][0] < target:
                l = m+1
            elif matrix[m][0] > target:
                r = m-1
            else:
                return True
        
        if matrix[m][0] > target:
            m = m-1

        r = len(matrix[m])-1
        l = m1 = 0
        while l <= r:
            m1 = l +((r-l)//2)
            if matrix[m][m1] < target:
                l = m1+1
            elif matrix[m][m1] > target:
                r = m1-1
            else:
                return True   
        return False