#User function Template for python3

class Solution:
    # Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self, arr):
        n = len(arr)
        current_sum = 0
        max_sum = arr[0]
        
        for i in range(n):
            current_sum += arr[i]
            max_sum = max(max_sum, current_sum)
            
            # Reset current_sum if it goes below 0
            if current_sum < 0:
                current_sum = 0
        
        return max_sum

            
        ##Your code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


def main():
    T = int(input())
    while (T > 0):

        arr = [int(x) for x in input().strip().split()]

        ob = Solution()

        print(ob.maxSubArraySum(arr))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends