
from typing import List


class Solution:
    def minimumCost(self, n : int, w : int, cost : List[int]) -> int:
        # code here
        dp=[float('inf') for i in range(w+1)]
        dp[0]=0
        for i in range(1,n+1):
            for j in range(i,w+1):
                if cost[i-1]==-1:
                    continue
                else:
                    dp[j]=min(cost[i-1]+dp[j-i],dp[j])
        #print(dp)
        return dp[-1]
        



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

        w = int(input())

        cost = IntArray().Input(n)

        obj = Solution()
        res = obj.minimumCost(n, w, cost)

        print(res)

# } Driver Code Ends