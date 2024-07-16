#User function Template for python3
class Solution:
    def maximumSumSubarray (self,K,Arr,N):
        max_sum = sum(Arr[:K])
        current_sum = max_sum
        for i in range(K,N):
            current_sum += Arr[i] - Arr[i-K]
            max_sum = max(current_sum,max_sum)
        return max_sum    
            
            
        # code here 


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        
        N,K = input().split()
        N = int(N)
        K = int(K)
        Arr = list( map(int,input().strip().split(" ")))

        ob = Solution()
        print(ob.maximumSumSubarray(K,Arr,N))
# } Driver Code Ends