#User function Template for python3

class Solution:
    
    #Function to find maximum of each subarray of size k.
    def max_of_subarrays(self,k,arr):
        
        #code here
        m=max(arr[:k])
        l=[m]
        for i in range(1,len(arr)-k+1):
            if(l[-1]!=arr[i-1]):
                if(l[-1]>arr[i+k-1]):
                    l.append(l[-1])
                else:
                    l.append(arr[i+k-1])
            else:
                l.append(max(arr[i:i+k]))
        return l

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys
from collections import deque

#Contributed by : Nagendra Jha

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        k = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        res = ob.max_of_subarrays(k, arr)
        for i in range(len(res)):
            print(res[i], end=" ")
        print()

# } Driver Code Ends