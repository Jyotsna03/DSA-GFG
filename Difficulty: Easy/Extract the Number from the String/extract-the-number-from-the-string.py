class Solution:
    def ExtractNumber(self,sentence):
        #code here
        numbers = list(map(int, filter(lambda x: x.isdigit() and "9" not in x, sentence.split())))
        return max(numbers) if numbers else -1


#{ 
 # Driver Code Starts
t = int(input())
for _ in range(t):
    S = input()
    ob = Solution()
    ans = ob.ExtractNumber(S)
    print(ans)

# } Driver Code Ends