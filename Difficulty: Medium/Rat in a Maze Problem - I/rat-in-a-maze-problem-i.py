from typing import List

class Solution:
    def findPath(self, m: List[List[int]]) -> List[str]:
        def is_safe(x, y):
            return 0 <= x < n and 0 <= y < n and m[x][y] == 1 and not visited[x][y]

        def solve(x, y, path):
            if x == n - 1 and y == n - 1:
                result.append(path)
                return
            
            # Mark the cell as visited
            visited[x][y] = True
            
            # Explore all possible directions
            for direction, move in moves.items():
                next_x, next_y = x + move[0], y + move[1]
                if is_safe(next_x, next_y):
                    solve(next_x, next_y, path + direction)
            visited[x][y] = False

        if not m or m[0][0] == 0:
            return []
        
        n = len(m)
        visited = [[False for _ in range(n)] for _ in range(n)]
        result = []
        
        # Possible moves (direction: (row_change, col_change))
        moves = {
            'U': (-1, 0),
            'D': (1, 0),
            'L': (0, -1),
            'R': (0, 1)
        }
        solve(0, 0, "")
        return result


#{ 
 # Driver Code Starts
# Main function to read input and output the results
if __name__ == "__main__":
    t = int(input().strip())
    for _ in range(t):
        n = int(input().strip())
        m = []
        for i in range(n):
            m.append(list(map(int, input().strip().split())))
        obj = Solution()
        result = obj.findPath(m)
        result.sort()
        if len(result) == 0:
            print(-1)
        else:
            print(" ".join(result))

# } Driver Code Ends