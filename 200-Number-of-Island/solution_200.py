class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        if not grid:
            return 0

        m = len(grid)
        n = len(grid[0])

        def search(i, j):
            if i < 0 or j < 0:
                return
            if i >= m or j >= n:
                return
            if grid[i][j] == "0":
                return

            grid[i][j] = "0"
            search(i + 1, j)
            search(i - 1, j)
            search(i, j + 1)
            search(i, j - 1)

        island_count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "0":
                    continue

                if grid[i][j] == "1":
                    island_count += 1
                    search(i, j)

        return island_count
