class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_island = 0
        R, C = len(grid), len(grid[0])
        for r in range(R):
            for c in range(C):
                if grid[r][c] != 1: # 0 or 2
                    continue
                island_size = self.exploreIsland(grid, r, c, R, C)
                if island_size > max_island:
                    max_island = island_size
        return max_island
        
    def exploreIsland(self, grid, r, c, R, C):
        if not self.validCoord(r, c, R, C) or grid[r][c] != 1: 
            return 0
        
        grid[r][c] = 2  # Mark visited
        count = 1       # Count current spot

        if self.validCoord(r-1, c, R, C) and grid[r-1][c] == 1:
            count += self.exploreIsland(grid, r-1, c, R, C)
        if self.validCoord(r+1, c, R, C) and grid[r+1][c] == 1:
            count += self.exploreIsland(grid, r+1, c, R, C)
        if self.validCoord(r, c-1, R, C) and grid[r][c-1] == 1:
            count += self.exploreIsland(grid, r, c-1, R, C)
        if self.validCoord(r, c+1, R, C) and grid[r][c+1] == 1:
            count += self.exploreIsland(grid, r, c+1, R, C)
        return count
        
        
    def validCoord(self, r, c, R, C):
        return r>=0 and c>=0 and r<=R-1 and c<=C-1
