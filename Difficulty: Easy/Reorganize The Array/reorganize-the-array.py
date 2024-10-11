#{ 
 # Driver Code Starts

# } Driver Code Ends

class Solution:
    def rearrange(self, arr):
        ne=set(arr)
        for i in range(len(arr)):
            if i in ne:
                arr[i]=i
            else:
                arr[i]=-1
        return arr

#{ 
 # Driver Code Starts.
def main():
    t = int(input())
    for _ in range(t):
        input_str = input()
        arr = list(map(int, input_str.split()))
        solution = Solution()
        ans = solution.rearrange(arr)
        print(" ".join(map(str, ans)))

if __name__ == "__main__":
    main()
# } Driver Code Ends