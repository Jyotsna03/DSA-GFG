#User function Template for python3
class Solution:
    def bracketNumbers(self, str):
        # code here
        stack=[]
        list1=[]
        count=1
        for i in str:
            if i=='(':
                stack.append(count)
                list1.append(count)
                count+=1
            elif i==')':
                popout=stack.pop()
                list1.append(popout)
        return list1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        S = input()
        ob = Solution()
        answer = ob.bracketNumbers(S)
        for value in answer:
            print(value, end=" ")
        print()

# } Driver Code Ends