//{ Driver Code Starts
//Initial Template for Java

import java.util.*;
import java.lang.*;
import java.io.*;

class GFG
{
	public static void main(String[] args) throws IOException
	{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine().trim());
        while(t-->0)
        {
            int n = Integer.parseInt(br.readLine().trim());
            int a[] = new int[(int)n];
            String inputLine[] = br.readLine().trim().split(" ");
            for (int i = 0; i < n; i++) {
                a[i] = Integer.parseInt(inputLine[i]);
            }
            
            Solution obj = new Solution();  
            System.out.println(obj.countPairs(a, n));
            
        }
	}
}

// } Driver Code Ends


//User function Template for Java


class Solution {
    public static int merge(int arr[], int low, int mid, int high) {
        int[] temp = new int[high - low + 1];
        int k = 0;
        int i = low;
        int j = mid + 1;
        int inv = 0;

        while (i <= mid && j <= high) {
            if (arr[i] <= arr[j]) {
                temp[k++] = arr[i++];
            } else {
                inv += mid - i + 1;
                temp[k++] = arr[j++];
            }
        }

        while (i <= mid) {
            temp[k++] = arr[i++];
        }

        while (j <= high) {
            temp[k++] = arr[j++];
        }

        for (int x = low; x <= high; x++) {
            arr[x] = temp[x - low];
        }

        return inv;
    }

    public static int mergeSort(int arr[], int low, int high) {
        if (low >= high)
            return 0;
        int inv = 0;

        int mid = (low + high) / 2;

        inv += mergeSort(arr, low, mid);
        inv += mergeSort(arr, mid + 1, high);
        inv += merge(arr, low, mid, high);

        return inv;
    }

    public static int inversionCount(int arr[], int N) {
        int ans = mergeSort(arr, 0, N - 1);
        return ans;
    }

    public static int countPairs(int arr[], int n) {
        for (int i = 0; i < n; i++) {
            arr[i] *= i;
        }
        return inversionCount(arr,n);
    }
}
