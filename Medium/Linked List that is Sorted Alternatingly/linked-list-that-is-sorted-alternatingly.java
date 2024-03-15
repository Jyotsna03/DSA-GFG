//{ Driver Code Starts
/*package whatever //do not write package name here */

import java.io.*;
import java.util.*;

class Node {
    int data;
    Node next;
    
    public Node (int data){
        this.data = data;
        this.next = null;
    }
}

class GFG {
    static void printList(Node node) 
	{ 
		while (node != null) 
		{ 
			System.out.print(node.data + " "); 
			node = node.next; 
		} 
		System.out.println(); 
	}
	public static void main (String[] args) {
		Scanner sc  = new Scanner(System.in);
		int t = sc.nextInt();
		while(t-- > 0){
		    int n = sc.nextInt();
		    
		    Node head = new Node(sc.nextInt());
		    Node tail = head;
		    
		    for(int i=1; i<n; i++){
		        tail.next = new Node(sc.nextInt());
		        tail = tail.next;
		    }
		    Solution obj = new Solution();
		    head = obj.sort(head);
		    printList(head);
		}
	}
}

// } Driver Code Ends



/*
class Node {
    int data;
    Node next;
    
    public Node (int data){
        this.data = data;
        this.next = null;
    }
}
*/

class Solution {
    
    public Node sort(Node head) {
        if (head == null || head.next == null) return head; // base case
        
        Node[] lists = splitList(head);
        Node ahead = lists[0];
        Node dhead = lists[1];
        
        dhead = reverse(dhead);
        
        head = merge(ahead, dhead);
        
        return head;
    }
    
    private Node merge(Node head1, Node head2) {
        if (head1 == null) return head2;  // base cases
        if (head2 == null) return head1;  // base cases
        
        Node temp = null;
        
        if (head1.data < head2.data) {
            temp = head1;  // picking the lower value
            temp.next = merge(head1.next, head2); // recursively merging the remaining list
        } else {
            temp = head2;  // picking the lower value
            temp.next = merge(head1, head2.next); // recursively merging the remaining list
        }
        return temp;
    }
    
    private Node reverse(Node head) {
        Node prev = null, curr = head, next = null;
        
        while (curr != null) {
            next = curr.next;
            curr.next = prev;
            prev = curr;
            curr = next;
        }
        
        return prev;
    }
    
    private Node[] splitList(Node head) {
        Node ahead = new Node(0);
        Node dhead = new Node(0);
        
        Node ascn = ahead;
        Node dscn = dhead;
        Node curr = head;
        
        while (curr != null) {
            ascn.next = curr;
            ascn = ascn.next;
            curr = curr.next;
            
            if (curr != null) {
                dscn.next = curr;
                dscn = dscn.next;
                curr = curr.next;
            }
        }
        
        ascn.next = null;
        dscn.next = null;
        
        ahead = ahead.next;
        dhead = dhead.next;
        
        return new Node[] {ahead, dhead};
        
    }
}