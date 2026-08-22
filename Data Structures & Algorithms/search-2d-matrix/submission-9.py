class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        print(target)
        l,r = 0, len(matrix)-1
        m = l +((r-l)//2)
        print(l,r, m)
        while l <= r:
            m = l +((r-l)//2)
            print(m, matrix[m][0])
            if matrix[m][0] < target:
                l = m+1
            elif matrix[m][0] > target:
                r = m-1
            else:
                return True
        
        if matrix[m][0] > target:
            m = m-1

        print('part2')
        l,r = 0, len(matrix[m])-1
        m1 =l +((r-l)//2)
        print(matrix[m], l,r,m1)
        while l <= r:
            m1 = l +((r-l)//2)
            #print(m, matrix[m][m1])
            if matrix[m][m1] < target:
                l = m1+1
            elif matrix[m][m1] > target:
                r = m1-1
            else:
                return True   
        return False