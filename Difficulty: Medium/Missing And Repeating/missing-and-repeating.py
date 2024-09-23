#User function Template for python3


class Solution:
    def findTwoElement( self,arr): 
        # code here
        arr.sort()
        p = 0
        for i in range(0,len(arr)-1):
            if arr[i] == arr[i+1]:
                p = arr[i]
        
        ans = 1        
        for i in range(0,len(arr)):
            if arr[i] == ans:
                ans += 1
                
        return [p,ans]   


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.findTwoElement(arr)
        print(str(ans[0]) + " " + str(ans[1]))
        tc = tc - 1

# } Driver Code Ends