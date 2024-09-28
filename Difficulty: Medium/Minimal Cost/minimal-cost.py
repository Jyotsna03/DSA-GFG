#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3
class Solution:
    def minimizeCost(self, k, arr):
        n = len(arr)
        dp = [float('inf')] * n
        dp[0] = 0  # Starting point
        
        for i in range(n):
            for j in range(i + 1, min(i + k + 1, n)):
                dp[j] = min(dp[j], dp[i] + abs(arr[i] - arr[j]))
        
        return dp[n - 1]
        # code here

#{ 
 # Driver Code Starts.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        k= int(input())
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.minimizeCost(k,arr)
        print(res)
        t -= 1


# } Driver Code Ends