#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3
#User function Template for python3
class Solution:
    #Function to return a list containing the union of the two arrays.
    def findUnion(self,a,b):
        # code here 
        ans=[]
        i,j=0,0
        while i<len(a) and j<len(b):
            if a[i]<b[j]:
                if not ans or ans[-1]!=a[i]:
                    ans.append(a[i])
                i+=1
            else:
                if not ans or ans[-1]!=b[j]:
                    ans.append(b[j])
                j+=1
        while i<len(a):
            if not ans or ans[-1]!=a[i]:
                ans.append(a[i])
            i+=1
        while j<len(b):
            if not ans or ans[-1]!=b[j]:
                ans.append(b[j])
            j+=1
        return ans

#{ 
 # Driver Code Starts.
if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        a = list(map(int, input().strip().split()))
        b = list(map(int, input().strip().split()))
        ob = Solution()
        li = ob.findUnion(a, b)
        for val in li:
            print(val, end=' ')
        print()
        print("~")
# } Driver Code Ends