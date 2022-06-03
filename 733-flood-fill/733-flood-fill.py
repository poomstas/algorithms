class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        R, C = len(image), len(image[0])
        queue = [[sr, sc]]
        startingCol = image[sr][sc]
        while len(queue):
            r, c = queue.pop()
            image[r][c] = newColor
            if self.validCoord(r+1, c, R, C) and image[r+1][c]==startingCol and image[r+1][c]!=newColor: # up
                queue.append([r+1, c])
            if self.validCoord(r-1, c, R, C) and image[r-1][c]==startingCol and image[r-1][c]!=newColor: # down
                queue.append([r-1, c])
            if self.validCoord(r, c-1, R, C) and image[r][c-1]==startingCol and image[r][c-1]!=newColor: # left
                queue.append([r, c-1])
            if self.validCoord(r, c+1, R, C) and image[r][c+1]==startingCol and image[r][c+1]!=newColor: # right
                queue.append([r, c+1])
        return image
    
    def validCoord(self, r, c, R, C):
        return r >= 0 and r < R and c >= 0 and c < C
    
        
