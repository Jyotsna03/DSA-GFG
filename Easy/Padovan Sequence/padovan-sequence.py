#User function Template for python3

class Solution:
    def padovanSequence(self, n):
        # code here 
        '''
        n = 3
        3 - 3 = 0 or 3 - 2 = 1
        4 - 3 = 1 or 4 - 2 = 2
        5 - 3 = 2 or 5 - 2 = 3
        '''
        MOD = 10 ** 9 + 7
        if n <= 2:
            return 1
    
        a,b,c,d = 1,1,1,1
        for i in range(3,n + 1):
            d = (a % MOD + b % MOD) % MOD
            a = b
            b = c
            c = d
        
        return d


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        ob = Solution()
        print(ob.padovanSequence(n))

# } Driver Code Ends