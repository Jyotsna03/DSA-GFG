#User function Template for python3

class Solution:
    # Function to sort a list using the Quick Sort algorithm.
    def quickSort(self, arr, low, high):
        if low < high:
            # Partition the array and get the pivot index
            pi = self.partition(arr, low, high)

            # Recursively sort elements before and after partition
            self.quickSort(arr, low, pi - 1)
            self.quickSort(arr, pi + 1, high)

    # Function to partition the array
    def partition(self, arr, low, high):
        pivot = arr[high]  # Choosing the last element as the pivot
        i = low - 1  # Index of the smaller element

        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]  # Swap

        arr[i + 1], arr[high] = arr[high], arr[i + 1]  # Swap pivot
        return i + 1  # Return the partition index
        # code here
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t=int(input())
    for i in range(t):
        n=int(input())
        arr=list(map(int,input().split()))
        Solution().quickSort(arr,0,n-1)
        for i in range(n):
            print(arr[i],end=" ")
        print()

# } Driver Code Ends