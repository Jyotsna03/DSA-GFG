//{ Driver Code Starts
// Initial Template for Java

import java.io.*;
import java.util.*;

public class GFG {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int tc = Integer.parseInt(br.readLine().trim());
        while (tc-- > 0) {
            String[] inputLine;
            inputLine = br.readLine().trim().split(" ");
            int n = Integer.parseInt(inputLine[0]);
            int[] arr = new int[n];
            inputLine = br.readLine().trim().split(" ");
            for (int i = 0; i < n; i++) {
                arr[i] = Integer.parseInt(inputLine[i]);
            }
            inputLine = br.readLine().trim().split(" ");
            int k = Integer.parseInt(inputLine[0]);
            int x = Integer.parseInt(inputLine[1]);

            int[] ans = new Solution().printKClosest(arr, n, k, x);
            for (int xx : ans) {
                System.out.print(xx + " ");
            }
            System.out.println();
        }
    }
}

// } Driver Code Ends


// User function Template for Java

class Solution {
    int[] printKClosest(int[] arr, int n, int k, int x) {
        // code here
        int res[]=new int[k];
        List<Integer> close=new ArrayList<>();
        int l=crossOver(arr,0,n-1,x);
        int r=l+1,count=0;
        
        if(arr[l]==x){
            l--;
        }
        
        while(l>=0 && r<n && count<k){
            if(x-arr[l]<arr[r]-x){
                close.add(arr[l]);
                l--;
            }
            else{
                close.add(arr[r]);
                r++;
            }
            
            count++;
        }
        
        while(count<k && l>=0){
            close.add(arr[l]);
            l--;
            count++;
        }
        
        while(count<k && r<n){
            close.add(arr[r]);
            r++;
            count++;
        }
        
        for(int i=0;i<k;i++){
            res[i]=close.get(i);
        }
        
        return res;
    }
    
    private int crossOver(int arr[],int l,int h,int x){
        if(arr[h]<=x){
            return h;
        }
        if(arr[l]>x){
            return l;
        }
        
        int mid=(l+h)/2;
        
        if(arr[mid]<=x && arr[mid+1]>x){
            return mid;
        }
        else if(arr[mid]<x){
            return crossOver(arr,mid+1,h,x);
        }
        
        return crossOver(arr,l,mid-1,x);
    }
}