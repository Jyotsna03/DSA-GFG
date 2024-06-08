from typing import List


class Solution:
    def countPartitions(self, n : int, d : int, arr : List[int]) -> int:
        # code here
        total = sum(arr)
        if((total - d) % 2):
            return 0
        target = (total - d)//2
        # print('target is ',target)
        if(target < 0):
            return 0
        table = [[0 for i in range(target+1)] for j in range(n+1)]
        for i in range(n+1):
            for j in range(target+1):
                if(i == 0 and j == 0):
                    table[i][j] = 1
                elif(i == 0 and j != 0):
                    table[i][j] = 0
                elif(j >= arr[i-1]):
                    table[i][j] = table[i-1][j - arr[i-1]] + table[i-1][j]
                else:
                    table[i][j] = table[i-1][j]
        # print(len(table), len(table[0]))
        return table[n][target]%(pow(10,9)+7)
        



#{ 
 # Driver Code Starts

class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        
        d = int(input())
        
        
        arr=IntArray().Input(n)
        
        obj = Solution()
        res = obj.countPartitions(n, d, arr)
        
        print(res)
        

# } Driver Code Ends