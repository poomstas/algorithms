class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        
        # Mark visited
        for r in range(R):
            _ = self.exploreEnclave(grid, r, 0, R, C)
            _ = self.exploreEnclave(grid, r, C-1, R, C)
        for c in range(C):
            _ = self.exploreEnclave(grid, 0, c, R, C)
            _ = self.exploreEnclave(grid, R-1, c, R, C)
        
        n_enclaves = 0
        for r in range(1, R-1):
            for c in range(1, C-1):
                if grid[r][c]==1:
                    n_enclave = self.exploreEnclave(grid, r, c, R, C)
                    n_enclaves += n_enclave
        return n_enclaves
        
    def exploreEnclave(self, grid, r, c, R, C):
        if not self.validCoord(r, c, R, C) or grid[r][c] != 1:
            return 0
        
        grid[r][c] = 2 # Mark visited land
        
        return 1 + \
            self.exploreEnclave(grid, r-1, c, R, C) + \
            self.exploreEnclave(grid, r+1, c, R, C) + \
            self.exploreEnclave(grid, r, c-1, R, C) + \
            self.exploreEnclave(grid, r, c+1, R, C)
    
    def validCoord(self, r, c, R, C):
        return r>=0 and c>=0 and r<=R-1 and c<=C-1
        
        
    ''' Faster to do DFS than to manually keep track of visits using separate array.
    def exploreEnclave(self, grid, r_i, c_i, R, C):
        n_enclave = 0
        queue = [[r_i, c_i]]
        while queue:
            r, c = queue.pop(0)
            if grid[r][c]==1:
                n_enclave += 1
            queue.extend(self.getLandNeighbors(grid, r, c, R, C))
            grid[r][c] = 2          # mark visited (2 is visited)
        return n_enclave
        
    def getLandNeighbors(self, grid, r, c, R, C):
        if grid[r][c]==0:
            return []
        neighbors = []
        if r > 0 and grid[r-1][c]==1:
            neighbors.append([r-1, c])
        if r < R-1 and grid[r+1][c]==1:
            neighbors.append([r+1, c])
        if c > 0 and grid[r][c-1]==1:
            neighbors.append([r, c-1])
        if c < C-1 and grid[r][c+1]==1:
            neighbors.append([r, c+1])
        return neighbors
    '''