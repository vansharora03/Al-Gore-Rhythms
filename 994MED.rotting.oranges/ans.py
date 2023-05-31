from queue import Queue
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = Queue()
        rows = len(grid)
        cols = len(grid[0])
        minutes = 0
        fresh = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    fresh += 1
                if grid[i][j] == 2:
                    q.put((i, j))
        
        if fresh == 0:
            return 0
        
        rottenGenIndicator = q.qsize()
        
        while q.qsize() > 0:
            x, y = q.get()

            directions = (0, 1), (0, -1), (1, 0), (-1, 0)

            for dx, dy in directions:
                r = x + dx
                c = y + dy
                if 0 <= r < rows and 0 <= c < cols and grid[r][c] == 1:
                    grid[r][c] += 1
                    fresh -= 1
                    q.put((r, c))

            rottenGenIndicator -= 1
            if rottenGenIndicator == 0:
                rottenGenIndicator = q.qsize()
                minutes += 1
        
        return minutes - 1 if fresh == 0 else -1