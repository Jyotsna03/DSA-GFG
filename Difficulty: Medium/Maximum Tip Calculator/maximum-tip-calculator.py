
from typing import List


class Solution:
    def maxTip(self, n : int, x : int, y : int, arr : List[int], brr : List[int]) -> int:
        # code here
        
        orders = [(abs(arr[i] - brr[i]), arr[i], brr[i], i) for i in range(n)]
        # Sort orders based on the absolute difference in descending order
        orders.sort(reverse=True, key=lambda x: x[0])
        
        total_tip = 0
        count_A, count_B = 0, 0
        
        for diff, tipA, tipB, index in orders:
            if (tipA >= tipB and count_A < x) or count_B == y:
                # Assign to A
                total_tip += tipA
                count_A += 1
            else:
                # Assign to B
                total_tip += tipB
                count_B += 1
                
        return total_tip






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

        x = int(input())

        y = int(input())

        arr = IntArray().Input(n)

        brr = IntArray().Input(n)

        obj = Solution()
        res = obj.maxTip(n, x, y, arr, brr)

        print(res)

# } Driver Code Ends