class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        R, C = len(grid), len(grid[0])
        self.visited = [[False for _ in range(C)] for _ in range(R)] # Boolean map
        island_count = 0
        
        for r in range(R):
            for c in range(C):
                if not self.visited[r][c] and grid[r][c]=='1':
                    self.traverseIsland(grid, r, c, R, C)
                    island_count += 1
                else:
                    self.visited[r][c] = True
        return island_count
        
    def traverseIsland(self, grid, r_init, c_init, R, C) -> None:
        queue = [[r_init, c_init]]
        while queue:
            r, c = queue.pop()
            self.visited[r][c] = True
            queue.extend(self.getValidIslandNeighbors(grid, r, c, R, C))
            
    def getValidIslandNeighbors(self, grid, r, c, R, C):
        neighbors = []
        if grid[r][c]=='0':
            return neighbors
        
        if r >= 1 and not self.visited[r-1][c] and grid[r-1][c]=='1':
            neighbors.append([r-1, c])
        if r < R-1 and not self.visited[r+1][c] and grid[r+1][c]=='1':
            neighbors.append([r+1, c])
        if c >= 1 and not self.visited[r][c-1] and grid[r][c-1]=='1':
            neighbors.append([r, c-1])
        if c < C-1 and not self.visited[r][c+1] and grid[r][c+1]=='1':
            neighbors.append([r, c+1])
            
        return neighbors
            
