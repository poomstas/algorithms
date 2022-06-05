class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        self.visited = [[False for _ in range(C)] for _ in range(R)]
        n_closed_island = 0
        for r in range(R):
            for c in range(C):
                if grid[r][c]==0:
                    if not self.visited[r][c]:
                        if self.determineClosed(grid, r, c, R, C):
                            n_closed_island += 1
                else:
                    self.visited[r][c] = True
        return n_closed_island
        
    def determineClosed(self, grid, r_i, c_i, R, C):
        queue = [[r_i, c_i]]
        closed = True
        while queue:
            r, c = queue.pop(0)
            if self.visited[r][c]:
                continue
            self.visited[r][c] = True
            queue.extend(self.getValidLandNeighbors(grid, r, c, R, C))
            if self.landTouchingBorder(grid, r, c, R, C):
                closed = False
        return closed
            
    def landTouchingBorder(self, grid, r, c, R, C):
        return True if r==0 or c==0 or r==R-1 or c==C-1 else False
        
    def getValidLandNeighbors(self, grid, r, c, R, C):
        neighbors = []
        if r > 0 and grid[r-1][c]==0:
            neighbors.append([r-1, c])
        if r < R-1 and grid[r+1][c]==0:
            neighbors.append([r+1, c])
        if c > 0 and grid[r][c-1]==0:
            neighbors.append([r, c-1])
        if c < C-1 and grid[r][c+1]==0:
            neighbors.append([r, c+1])
        return neighbors
        