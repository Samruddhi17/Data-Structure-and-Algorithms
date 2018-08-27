class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        count=0
        rows = len(grid)
        columns = len(grid[0])
        
        for i in range(rows):
            for j in range(columns):
                if grid[i][j]=='1':
                    self.dfs(grid,i,j)
                    count+=1
        return count
    
    def dfs(self, grid, i, j):
        if i<0 or i>len(grid)-1 or j<0 or j>len(grid[0])-1 or grid[i][j]!='1':
            return
        else:
            grid[i][j]='#'
            self.dfs(grid,i+1,j)
            self.dfs(grid,i-1,j)
            self.dfs(grid,i,j+1)
            self.dfs(grid,i,j-1)