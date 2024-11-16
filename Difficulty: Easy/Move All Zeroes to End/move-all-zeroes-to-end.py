#User function Template for python3

class Solution:
    def pushZerosToEnd(self,arr):
        temp = []
        zero = 0
        for i in arr:
            if i==0:
                zero +=1
            else:
                temp.append(i)
        t = len(temp)
        for i in range(t):
            arr[i] = temp[i]
        for i in range(t, t+zero):
            arr[i] = 0


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.pushZerosToEnd(arr)
        for x in arr:
            print(x, end=" ")
        print()
        tc -= 1
# } Driver Code Ends