#Your task is to complete this function
#Function should return an integer denoting the required answer
class Solution:
    def maxPathSum(self, arr1, arr2):
        # Code here
        i=j=s1=s2=ans=0
        n=len(arr1)
        m=len(arr2)
        while i<n or j<m:
            if j==m:
                s1+=arr1[i]
                i+=1
                continue 
            if i==n:
                s2+=arr2[j]
                j+=1
                continue 
            if arr1[i]>arr2[j]:
                s2+=arr2[j]
                j+=1
            elif arr1[i]<arr2[j]:
                s1+=arr1[i]
                i+=1
            else:
                s1+=arr1[i]
                i+=1
                s2+=arr2[j]
                j+=1
                ans+=max(s1,s2)
                s1=s2=0
        ans+=max(s1,s2)
        return ans



#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input().strip())
    for _ in range(t):
        arr1 = list(map(int, input().strip().split()))
        arr2 = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.maxPathSum(arr1, arr2)
        print(ans)

# } Driver Code Ends