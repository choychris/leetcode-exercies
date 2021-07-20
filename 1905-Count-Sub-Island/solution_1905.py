class Solution:
    def countSubIslands(self, grid1: list[list[int]], grid2: list[list[int]]) -> int:
        m = len(grid1)
        n = len(grid1[0])

        if m == 1 and n == 1:
            if grid1[0][0] == 1 and grid2[0][0]:
                return 1

        def build_island(island, i, j):
            if i < 0 or j < 0:
                return
            if i >= m or j >= n:
                return
            if not grid2[i][j]:
                return

            island.append([i, j])
            grid2[i][j] = None
            build_island(island, i + 1, j)
            build_island(island, i - 1, j)
            build_island(island, i, j + 1)
            build_island(island, i, j - 1)

        island_match = 0
        for i in range(m):
            for j in range(n):
                if not grid2[i][j]:
                    continue

                if grid2[i][j] == 1:
                    island = []
                    build_island(island, i, j)

                    if len(island) > 0:
                        match = 0
                        for land in island:
                            if grid1[land[0]][land[1]]:
                                match += 1

                        if match == len(island):
                            island_match += 1

        return island_match
