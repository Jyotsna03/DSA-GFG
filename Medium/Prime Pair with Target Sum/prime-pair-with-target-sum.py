from typing import List
import math
def f(n):
    if n==1:
        return 0
    if n==2:
        return 1
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return 0 
    return 1
    
class Solution:
    def getPrimes(self, n : int) -> List[int]:
        # code here
        if n&1:
            if f(n-2)==1:
                return [2,n-2]
            return [-1,-1]
        else:
            for i in range(2,n//2+1):
                if f(i)==1 and f(n-i)==1:
                    return [i,n-i]

            return [-1,-1]



#{ 
 # Driver Code Starts
class IntArray:

    def __init__(self) -> None:
        pass

    def Input(self, n):
        arr = [int(i) for i in input().strip().split()]  #array input
        return arr

    def Print(self, arr):
        for i in arr:
            print(i, end=" ")
        print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        n = int(input())

        obj = Solution()
        res = obj.getPrimes(n)

        IntArray().Print(res)

# } Driver Code Ends