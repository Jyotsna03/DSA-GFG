#User function Template for python3
#User function Template for python3

class Solution:
    def sumMatrix(self, n, q):
        r=abs(q-(n+1))
        if ( n-r)<=0:
            return 0
        else:
            return (n-r)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, q = map(int, input().split())

        ob = Solution()
        print(ob.sumMatrix(n, q))

# } Driver Code Ends