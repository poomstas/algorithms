class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.R, self.C = len(grid), len(grid[0])
        island_count = 0
        self.visited = [[False for _ in range(self.C)] for _ in range(self.R)] # Boolean map
        for r in range(self.R):
            for c in range(self.C):
                if not self.visited[r][c] and grid[r][c]=='1':
                    self.exploreIsland(grid, r, c)
                    island_count += 1
                else:
                    self.visited[r][c] = True
        return island_count
        
    def exploreIsland(self, grid: List[List[str]], r_init: int, c_init: int) -> None:
        queue = [[r_init, c_init]]
        while queue:
            r, c = queue.pop()
            self.visited[r][c] = True
            queue.extend(self.getValidIslandNeighbors(grid, r, c))
            
    def getValidIslandNeighbors(self, grid, r, c):
        neighbors = []
        if grid[r][c]=='0':
            return neighbors
        
        if r >= 1 and not self.visited[r-1][c] and grid[r-1][c]=='1':
            neighbors.append([r-1, c])
        if r < self.R-1 and not self.visited[r+1][c] and grid[r+1][c]=='1':
            neighbors.append([r+1, c])
        if c >= 1 and not self.visited[r][c-1] and grid[r][c-1]=='1':
            neighbors.append([r, c-1])
        if c < self.C-1 and not self.visited[r][c+1] and grid[r][c+1]=='1':
            neighbors.append([r, c+1])
            
        return neighbors
            
        