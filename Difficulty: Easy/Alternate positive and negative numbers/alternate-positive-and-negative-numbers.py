#User function Template for python3

class Solution:
    def rearrange(self,arr):
        # code here
        pos=[x for x in arr if x>=0]
        neg=[x for x in arr if x<0]
        ans=[]
        i,j=0,0
        while i< len(pos) or j<len(neg):
            if i <len(pos):
                ans.append(pos[i])
                i+=1
            if j < len(neg):
                ans.append(neg[j])
                j+=1
        for k in range(len(arr)):
            arr[k]=ans[k]
        return arr
                
        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.rearrange(arr)
        for x in arr:
            print(x, end=" ")
        print()
        tc -= 1

# } Driver Code Ends