#User function Template for python3

#User function Template for python3

class Solution:
    def minIncrements(self, arr): 
        arr.sort()  # Sort the array
        increments = 0

        for i in range(1, len(arr)):
            if arr[i] <= arr[i - 1]:
                needed_increment = arr[i - 1] - arr[i] + 1
                arr[i] += needed_increment
                increments += needed_increment
    
        return increments



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    T = int(input())
    while T > 0:
        arr = [int(i) for i in input().split()]
        ob = Solution()
        print(ob.minIncrements(arr))

        T -= 1

# } Driver Code Ends