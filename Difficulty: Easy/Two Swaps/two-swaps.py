class Solution:
    def mismatches(self,arr):
        arr1=sorted(arr)
        mismatch=[i for i in range(len(arr)) if arr[i]!=arr1[i]]
        return mismatch
    def swaponce(self,arr):
        for i in range(len(arr)):
            if arr[i]!=i+1:
                for j in range(i+1,len(arr)):
                    if arr[j]==i+1:
                        arr[j],arr[i]=arr[i],arr[j]
                        return
    def checkSorted(self,arr):
        n=len(arr)
        mismatch=self.mismatches(arr)
        if len(mismatch)==1 or len(mismatch)==2 or len(mismatch)>4:
            return False
        if len(mismatch)==3 or len(mismatch)==4 or len(mismatch)==0:
            self.swaponce(arr)
            self.swaponce(arr)
            if len(self.mismatches(arr))==0:
                return True
            return False
            


#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input().strip())

    for _ in range(t):
        arr = list(map(int, input().split()))

        sol = Solution()
        result = sol.checkSorted(arr)
        if result:
            print("true")
        else:
            print("false")

# } Driver Code Ends