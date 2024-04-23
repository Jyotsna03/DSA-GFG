//{ Driver Code Starts
// Initial Template for Java
import java.io.*;
import java.util.*;

class GFG {
    public static void main(String args[]) throws IOException {
        BufferedReader read = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(read.readLine());
        while (t-- > 0) {
            int n = Integer.parseInt(read.readLine());
            Solution ob = new Solution();
            System.out.println(ob.firstElement(n));
        }
    }
}
// } Driver Code Ends


// User function Template for Java
class Solution {
    static int firstElement(int n) {
        // Define the given matrix A
        int[][] A = {{1, 1}, {1, 0}};
        
        // Initialize the result matrix as the identity matrix
        int[][] result = {{1, 0}, {0, 1}};
        
        // Perform matrix exponentiation
        while (n > 0) {
            if (n % 2 == 1) {
                result = multiply(result, A);
            }
            A = multiply(A, A);
            n /= 2;
        }
        
        // The element at index (1, 0) in the resulting matrix is the answer
        return result[1][0] % 1000000007;
    }
    
    // Function to multiply two matrices
    static int[][] multiply(int[][] A, int[][] B) {
        int[][] C = new int[2][2];
        for (int i = 0; i < 2; i++) {
            for (int j = 0; j < 2; j++) {
                for (int k = 0; k < 2; k++) {
                    C[i][j] = (int)((C[i][j] + (long)A[i][k] * B[k][j]) % 1000000007);
                }
            }
        }
        return C;
   }
}