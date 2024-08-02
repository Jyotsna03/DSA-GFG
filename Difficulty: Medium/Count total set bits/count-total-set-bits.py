class Solution:
    #Function to return sum of count of set bits in the integers from 1 to n.
    def countSetBits(self, n):
        def largestPower(n):
            x = 0
            while (1 << x) <= n:
                x += 1
            
            return (x - 1)
        
        def solve(n):
            if n == 0:
                return 0
            x = largestPower(n)
            bitsUpto = x * (2 ** (x - 1))
            msbFrom = n - (2 ** x) + 1
            res = bitsUpto + msbFrom + solve(n - (2 ** x))
            return res
        
        return int(solve(n))

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    for _ in range(int(input())):
        ob=Solution()
        print(ob.countSetBits(int(input())))
# } Driver Code Ends