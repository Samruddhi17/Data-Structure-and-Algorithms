class Solution:
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        max_score =4
        peri =0
        rows = len(grid)
        columns = len(grid[0])
        
        for i in range(rows):
            for j in range(columns):
                if grid[i][j]==1:
                    max_score =4
                    if i>0 :
                        if grid[i-1][j]==1:
                            max_score -=1
                    if i<rows-1:
                        if grid[i+1][j]==1:
                            max_score -=1
                    if j>0:
                        if grid[i][j-1]==1:
                            max_score -=1
                    if j<columns-1:
                        if grid[i][j+1]==1:
                            max_score -=1
                    peri+=max_score
        return peri