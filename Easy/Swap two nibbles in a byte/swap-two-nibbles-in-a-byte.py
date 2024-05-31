#User function Template for python3
class Solution:
    def swapNibbles (self, n):
        # code here 
        
        b = bin(n)[2:]
        
        l = len(b)
        diff = 8-l
        
        b = '0'*diff + b
            
        b1 = b[0:4]
        b2 = b[4:]
        
        bnew = b2+b1
        
        n1 = int(bnew,2)
        return n1

#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())

        ob = Solution()
        print(ob.swapNibbles(n))

# } Driver Code Ends