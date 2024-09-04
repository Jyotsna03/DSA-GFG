#User function Template for python3
class Solution:
    def nthStair(self,n):
        dp = [-1]*(n+1)
        
        def solve(n):
            if n<0:
                return 0
            if n<=1:
                return 1
            if dp[n] != -1:
                return dp[n]
            dp[n] = 1 + solve(n-2)
            return dp[n]
        
        return solve(n)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		ob = Solution();
		ans = ob.nthStair(n)
		print(ans)
# } Driver Code Ends