#User function Template for python3

class Solution:
    def maxSum(self,arr):
        # code here
        arr.sort()
        
        i=0
        j=len(arr)-1
        
        res = 0
        turn = 0
        while i<j:
            res += arr[j]-arr[i]
            
            if turn == 0:
                i += 1
            else:
                j -= 1
            
            turn = 1-turn
            
        res += arr[j]-arr[0]
        
        return res


#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.maxSum(arr)  # Call maxSum method and store result in ans
        print(ans)  # Print the result
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends