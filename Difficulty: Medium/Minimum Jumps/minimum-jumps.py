#User function Template for python3
class Solution:
    def minJumps(self, arr):
        length = len(arr)
        if length == 0 or arr[0] == 0:
            return -1 
        
        if length == 1:
            return 0  
        jumps = 0  
        current_end = 0 
        farthest = 0  
        
        for i in range(length):
            farthest = max(farthest, i + arr[i])
            
            if i == current_end:
                if i != length - 1:
                    jumps += 1
                    current_end = farthest
                if current_end >= length - 1:
                    return jumps
        
        return -1 



#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        # n = int(input())
        Arr = [int(x) for x in input().split()]
        ob = Solution()
        ans = ob.minJumps(Arr)
        print(ans)

# } Driver Code Ends