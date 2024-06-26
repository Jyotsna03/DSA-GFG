#User function Template for python3


class Solution:
    def merge(self, arr, l, m, r): 
        temp = []
        i, j = l, m + 1
        while i <= m and j <= r:
            if arr[i] <= arr[j]:
                temp.append(arr[i])
                i += 1
            else:
                temp.append(arr[j])
                j += 1
        
        while i <= m:
            temp.append(arr[i])
            i += 1
            
        while j <= r:
            temp.append(arr[j])
            j += 1
        
        for i in range(len(temp)):
            arr[l + i] = temp[i]
        
    def mergeSort(self, arr, l, r):
        if l < r:
            m = (l + r) // 2
            self.mergeSort(arr, l, m)
            self.mergeSort(arr, m + 1, r)
            self.merge(arr, l, m, r)



#{ 
 # Driver Code Starts
#Initial Template for Python 3


import sys
input = sys.stdin.readline
if __name__ == "__main__":
    t=int(input())
    for i in range(t):
        n=int(input())
        arr=list(map(int,input().split()))
        Solution().mergeSort(arr, 0, n-1)
        for i in range(n):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends