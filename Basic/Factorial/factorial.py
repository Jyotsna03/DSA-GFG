#User function Template for python3

import math
class Solution:
    def factorial (self, N):
        ans = math.factorial(N)
        return ans
        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
        ob = Solution()
        print(ob.factorial(N))

# } Driver Code Ends