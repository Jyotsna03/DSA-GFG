#User function Template for python3

class Solution:
    def productExceptSelf(self, nums):
        #code here
        length = len(nums)
        result = [1] * length
        prefix = 1
        for i in range(length):
            result[i] = prefix
            prefix *= nums[i]
        suffix = 1
        for i in range(length - 1, -1, -1):
            result[i] *= suffix
            suffix *= nums[i]
    
        return result


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        n = int(input())
        arr = [int(x) for x in input().split()]

        ans = Solution().productExceptSelf(arr)
        print(*ans)

# } Driver Code Ends