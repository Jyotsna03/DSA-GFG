#User function Template for python3
from typing import List

class Solution:
    def print2largest(self, arr: List[int]) -> int:
        # Convert array to set to get distinct elements
        distinct_elements = list(set(arr))
        
        # Check if there are at least two distinct elements
        if len(distinct_elements) < 2:
            return -1
        
        # Sort the distinct elements in descending order
        distinct_elements.sort(reverse=True)
        
        # Return the second largest element
        return distinct_elements[1]


#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.print2largest(arr)
        print(ans)

# } Driver Code Ends