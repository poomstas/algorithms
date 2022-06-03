class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.R, self.C = len(grid), len(grid[0])
        self.visited = [[False for _ in range(self.C)] for _ in range(self.R)]
        max_area = 0
        for r in range(self.R):
            for c in range(self.C):
                if grid[r][c]==1:
                    area = self.exploreIsland(grid, r, c)
                    if area > max_area:
                        max_area = area
        return max_area
    
    def exploreIsland(self, grid, r_init, c_init):
        island_area = 0
        queue = [[r_init, c_init]]
        while queue:
            r, c = queue.pop(0)
            if self.visited[r][c] == True:
                continue
            self.visited[r][c] = True
            island_area += 1
            queue.extend(self.getValidIslandNeighbors(grid, r, c))
        return island_area
    
    def getValidIslandNeighbors(self, grid, r, c):
        neighbors = []
        if grid[r][c]==0:
            return neighbors
        if r > 0 and grid[r-1][c]==1 and not self.visited[r-1][c]:
            neighbors.append([r-1, c])
        if r < self.R-1 and grid[r+1][c]==1 and not self.visited[r+1][c]:
            neighbors.append([r+1, c])
        if c > 0 and grid[r][c-1]==1 and not self.visited[r][c-1]:
            neighbors.append([r, c-1])
        if c < self.C-1 and grid[r][c+1]==1 and not self.visited[r][c+1]:
            neighbors.append([r, c+1])
        return neighbors
