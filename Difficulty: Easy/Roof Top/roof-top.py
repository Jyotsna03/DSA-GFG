#User function Template for python3

class Solution:
    
    #Function to find maximum number of consecutive steps 
    #to gain an increase in altitude with each step.
   def maxStep(self, arr):
        count = res = 0
        
        for index, step in enumerate(arr[:-1]):
            if arr[index + 1] - step > 0:
                count += 1
            else:
                count = 0
            res = max(res, count)
        
        return res


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


def main():
    T = int(input())
    while (T > 0):

        arr = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.maxStep(arr))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends