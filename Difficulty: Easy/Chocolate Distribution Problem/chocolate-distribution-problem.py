#User function Template for python3

class Solution:

    def findMinDiff(self, arr, n, m):
        arr.sort() #O(nlogn) work
        i = 0
        j = m - 1
        minNum = float('inf')
        while j < n:
            minNum = min(minNum, arr[j] - arr[i])
            i += 1
            j += 1
        
        return minNum
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        N = int(input())
        A = [int(x) for x in input().split()]
        M = int(input())


        solObj = Solution()

        print(solObj.findMinDiff(A,N,M))
# } Driver Code Ends