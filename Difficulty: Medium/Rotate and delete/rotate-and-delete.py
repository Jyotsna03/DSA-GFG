#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends

# from typing import List


class Solution:
    def rotateDelete(self,  arr):
        n = len(arr)
        sz = n//2
        
        for i in range(sz):
            arr = [arr[-1]] + arr[0:(len(arr)-1)]
            arr.pop(len(arr)-i-1)
            
        return arr[0]
        


#{ 
 # Driver Code Starts.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.rotateDelete(arr)
        print(res)
        t -= 1


# } Driver Code Ends