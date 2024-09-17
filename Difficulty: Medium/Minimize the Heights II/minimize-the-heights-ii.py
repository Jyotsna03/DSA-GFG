#User function Template for python3


class Solution:
    def getMinDiff(self, arr, k):
        # Sort the array to manage elements in a linear way
        arr.sort()
        n = len(arr)
        
        # The initial difference between the max and min elements
        result = arr[-1] - arr[0]

        # Iterate through the array to find the optimal way to add/subtract k
        for i in range(1, n):
            if arr[i] >= k:
                max_element = max(arr[i-1] + k, arr[-1] - k)
                min_element = min(arr[0] + k, arr[i] - k)
                result = min(result, max_element - min_element)
        
        return result


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        k = int(input())
        # n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.getMinDiff(arr, k)
        print(ans)
        tc -= 1

# } Driver Code Ends