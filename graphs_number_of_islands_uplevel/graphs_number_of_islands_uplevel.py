# ************************ Graph: Number of Islands *********************************
# DAM 12/13/2021
# Given a binary search tree (BST) and an integer k, find k-th smallest element.
import collections

def numIslands(grid):

    def getNeighbors(x, y):
        result = []

        if x + 1 < len(grid):
            result.append((x + 1, y))

        if y + 1 < len(grid[0]):
            result.append((x, y + 1))

        if x - 1 >= 0:
            result.append((x - 1, y))

        if y - 1 >= 0:
            result.append((x, y - 1))

        return result

    def bfs(i, j):
        q = collections.deque()
        q.append((i, j))
        grid[i][j] = '0'

        while len(q) != 0:
            (row, col) = q.popleft()
            neighbors = getNeighbors(row, col)

            for (nr, nc) in neighbors:
                if grid[nr][nc] != '0':
                    q.append((nr, nc))
                    grid[nr][nc] = '0'

    islands = 0

    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if grid[x][y] != '0':
                bfs(x, y)
                islands += 1

    return islands

print(numIslands([[1,1,0,0,0],[0,1,0,0,1],[1,0,0,1,1],[0,0,0,0,0],[1,0,1,0,1]]))

