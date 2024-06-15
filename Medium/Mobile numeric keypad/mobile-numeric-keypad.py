#User function Template for python3
#User function Template for python3
class Solution:
    def getCount(self, n):
        # code here
        if n == 1:
            return 10

        moves = {
            0: [0, 8],
            1: [1, 2, 4],
            2: [1, 2, 3, 5],
            3: [2, 3, 6],
            4: [1, 4, 5, 7],
            5: [2, 4, 5, 6, 8],
            6: [3, 5, 6, 9],
            7: [4, 7, 8],
            8: [0, 5, 7, 8, 9],
            9: [6, 8, 9]
        }

        count = [1] * 10
        for _ in range(2, n + 1):
            new_count = [0] * 10
            for i in range(10):
                for j in moves[i]:
                    new_count[i] += count[j]
            count = new_count

        return sum(count)



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n = int(input())
        ob = Solution()
        ans = ob.getCount(n)
        print(ans)

# } Driver Code Ends