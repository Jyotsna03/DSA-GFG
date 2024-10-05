#User function Template for python3


class Solution:
    def findSmallest(self, arr):
        # Initialize result with 1
        res = 1
        
        # Traverse the array
        for num in arr:
            # If current number is greater than res, we can't form 'res'
            if num > res:
                break
            # Otherwise, add the current number to res
            res += num
        
        return res


#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.findSmallest(arr)
        print(ans)


if __name__ == "__main__":
    main()

# } Driver Code Ends