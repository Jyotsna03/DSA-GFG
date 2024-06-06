#User function Template for python3

def max_sum(a,n):
    #code here
    total_sum = sum(a)
    max_sum  = 0
    for i in range(n):
        max_sum += i*a[i]
    max_val = max_sum
    for j in range(1,n):
        max_sum += total_sum - n * arr[n-j]
        max_val = max(max_val,max_sum)
    return max_val


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        print(max_sum(arr, n))

# } Driver Code Ends