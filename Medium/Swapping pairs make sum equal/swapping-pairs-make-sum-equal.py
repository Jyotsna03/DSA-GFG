class Solution:
    def findSwapValues(self,a, n, b, m):
        sum_a=sum(a)
        sum_b=sum(b)
        set_a=set(a)
        set_b=set(b)
        tar=(sum_a-sum_b)/2
        for i in set_b:
            if tar+i in set_a:
                return 1
        return -1

#{ 
 # Driver Code Starts
if __name__ == '__main__': 
    
    
    t=int(input())
    for _ in range(0,t):
        l=list(map(int,input().split()))
        n=l[0]
        m=l[1]
        a = list(map(int,input().split()))
        b = list(map(int, input().split()))
        ob = Solution()
        print(ob.findSwapValues(a,n,b,m))
# } Driver Code Ends