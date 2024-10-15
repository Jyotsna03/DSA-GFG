#User function template for Python 3

class Solution:
    def majorityElement(self, arr):
        hash = {}
        majority = len(arr) // 2  # Majority threshold
        for num in arr:
            hash[num] = 1 + hash.get(num, 0)
            if hash[num] > majority:
                return num  # Early return if majority found

        return -1 
            
        #Your code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

from sys import stdin


def main():
    T = int(input())
    while (T > 0):

        A = [int(x) for x in input().strip().split()]

        obj = Solution()
        print(obj.majorityElement(A))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends