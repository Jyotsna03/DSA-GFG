# Your task is to complete this function
# Function should return true/false
def PalinArray(arr):
    for i in arr:
        if str(i)!=str(i)[::-1]:
            return False
    return True    
        
    # Code here



#{ 
 # Driver Code Starts
# Driver Program
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        arr = list(map(int, input().strip().split()))
        if PalinArray(arr):
            print("true")
        else:
            print("false")
# Contributed By: Harshit Sidhwa

# } Driver Code Ends