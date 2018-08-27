class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []
        output=[]
        r1 =0
        c1= 0
        r2 = len(matrix)
        c2 = len(matrix[0])
        
        while r1<=r2-1 and c1<=c2-1:
            for i in range(c1,c2):
                output.append(matrix[r1][i])
                
            for i in range(r1+1,r2):
                output.append(matrix[i][c2-1])
                
            if r1<r2-1 and c1< c2-1:
                for i in range(c2-2,c1,-1):
                    output.append(matrix[r2-1][i])
                    
                for i in range(r2-1,r1,-1):
                    output.append(matrix[i][c1])
                
            r1,r2,c1,c2=r1+1,r2-1,c1+1,c2-1
        return output
   