#User function Template for python3

class Solution:
    def numIslands(self, grid):
        # code here
        n = len(grid)
        m = len(grid[0])
    
    # Directions for 8 neighbors (up, down, left, right, 4 diagonals)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    
    # DFS function to visit all connected land cells (iterative version)
        def dfs_iterative(i, j):
        # Stack to simulate recursion
            stack = [(i, j)]
        
            while stack:
                ci, cj = stack.pop()
            
            # If out of bounds or in water, continue
                if ci < 0 or ci >= n or cj < 0 or cj >= m or grid[ci][cj] == 0:
                    continue
            
            # Mark current land as visited by setting it to 0
                grid[ci][cj] = 0
            
            # Push all 8 neighbors to stack
                for di, dj in directions:
                    stack.append((ci + di, cj + dj))
    
    # Initialize island count
        island_count = 0
    
    # Iterate through the grid
        for i in range(n):
            for j in range(m):
                # If we find land ('1'), it's a new island
                if grid[i][j] == 1:
                    # Increment island count and start DFS (iterative)
                    island_count += 1
                    dfs_iterative(i, j)
    
        return island_count




#{ 
 # Driver Code Starts
# Driver code
if __name__ == "__main__":
    for _ in range(int(input())):
        n, m = map(int, input().strip().split())
        grid = []
        for i in range(n):
            grid.append([int(i) for i in input().strip().split()])
        obj = Solution()
        print(obj.numIslands(grid))

# } Driver Code Ends