#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends



class Solution:
    def removeDuplicates(self, arr):
        seen = [False] * 101
        output = []
        for e in arr:
            if not seen[e]:
                seen[e] = True
                output.append(e)
        return output
        

#{ 
 # Driver Code Starts.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.removeDuplicates(arr)
        print(*ans)
        print("~")
        t -= 1


# } Driver Code Ends