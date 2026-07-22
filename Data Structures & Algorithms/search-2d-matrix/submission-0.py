class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
 
        for i in range(len(matrix)):
            if (i == len(matrix)-1) or (matrix[i][0] <= target and target < matrix[i+1][0]):
                col = i
                l, r = 0, len(matrix[col])-1
                
                while l <= r:
                    m = l + ((r-l)//2)

                    if target < matrix[i][m]:
                        r = m-1
                    elif target > matrix[i][m]:
                        l = m+1
                    else:
                        return True
        
        return False
            

            