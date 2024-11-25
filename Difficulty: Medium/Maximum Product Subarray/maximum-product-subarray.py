#User function Template for python3
#User function Template for python3
class Solution:

    # Function to find maximum
    # product subarray
    def maxProduct(self,arr):
        max_product = min_product = result = arr[0]
        for num in arr[1:]:
            max_product, min_product = max(num, max_product * num, min_product * num), min(num, max_product * num, min_product * num)
            result = max(result, max_product)
        return result
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.maxProduct(arr)
        print(ans)
        tc -= 1

# } Driver Code Ends