class Solution:
    # Function to find the majority elements in the array
    def findMajority(self, arr):
        #Your Code goes here.
        n = len(arr)
        thresh = n // 3
        
        maj_1 = None
        maj_1_cnt = 0
        
        maj_2 = None
        maj_2_cnt = 0
        
        for num in arr:
            if num == maj_1:
                maj_1_cnt += 1
            elif num == maj_2:
                maj_2_cnt += 1
            elif maj_1_cnt == 0:
                maj_1 = num
                maj_1_cnt += 1
            elif maj_2_cnt == 0:
                maj_2 = num
                maj_2_cnt += 1
            else:
                maj_1_cnt -= 1
                maj_2_cnt -= 1

        res = []
        for c in [maj_1, maj_2]:
            if arr.count(c) > n // 3:
                res.append(c)

        return sorted(res)

#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():
    t = int(input().strip())
    for _ in range(t):
        s = input().strip()
        nums = list(map(int, s.split()))
        ob = Solution()
        ans = ob.findMajority(nums)
        if not ans:
            print("[]")
        else:
            print(" ".join(map(str, ans)))


if __name__ == "__main__":
    main()

# } Driver Code Ends