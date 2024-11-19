#User function Template for python3

#User function Template for python3

class Solution:
    def nextPermutation(self, arr):
        # code here
        for i in range(len(arr)-2,-1,-1):
            if arr[i]<arr[i+1]:
                break
        if arr[i]>=arr[i+1]:
            arr.sort()
            return 
        s_inx = i+1
        for j in range(i+1,len(arr)):
            if arr[j]>arr[i]:
                if arr[j]<arr[s_inx]:
                    s_inx  = j
        # print(i,s_inx)
        arr[i] , arr[s_inx] = arr[s_inx] , arr[i]
        s = i+1
        e = len(arr)-1
        
        while s<=e:
            arr[s],arr[e] = arr[e],arr[s]
            s+=1
            e-=1
            
        
                
                
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        arr = input().split()
        N = len(arr)
        for i in range(N):
            arr[i] = int(arr[i])

        ob = Solution()
        ob.nextPermutation(arr)
        for i in range(N):
            print(arr[i], end=" ")
        print()

# } Driver Code Ends