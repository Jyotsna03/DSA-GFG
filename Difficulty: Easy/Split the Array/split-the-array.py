#User function Template for python3
class Solution:
    def countgroup(self,arr): 
        #Complete the function
        x=0
        for i in arr:
            x^=i
        if x==0:
            return (2**(len(arr)-1))-1
        else:
            return 0



#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.countgroup(arr)
        print(res)
        t -= 1

# } Driver Code Ends