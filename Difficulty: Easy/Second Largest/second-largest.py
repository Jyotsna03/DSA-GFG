#User function Template for python3
class Solution:
    def getSecondLargest(self, arr):
        # Code Here
        arr=list(set(arr))
        arr1=sorted(arr)
        if len(arr1)>=2:
            return arr1[-2]
        return -1


#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.getSecondLargest(arr)
        print(ans)
        print("~")
# } Driver Code Ends