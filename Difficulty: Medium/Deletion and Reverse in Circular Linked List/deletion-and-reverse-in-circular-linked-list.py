#User function Template for python3
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''
class Solution:
    # Function to delete a node with a given key from the circular linked list
    def deleteNode(self, head, key):
        if not head:
            return None
        
        curr = head
        prev = None
        
        # Case 1: If the list contains only one node and that node has the key
        if head.data == key and head.next == head:
            return None

        # Case 2: If the node to be deleted is the head
        if head.data == key:
            prev = head
            # Find the last node
            while prev.next != head:
                prev = prev.next
            # Point the last node to the next of head and return the new head
            prev.next = head.next
            head = head.next
            return head
        
        # Case 3: The key is somewhere other than the head
        while curr.next != head and curr.data != key:
            prev = curr
            curr = curr.next

        # If the node was found, delete it
        if curr.data == key:
            prev.next = curr.next

        return head

    # Function to reverse the circular linked list
    def reverse(self, head):
        if not head or head.next == head:
            return head
        
        prev = None
        curr = head
        next_node = None
        
        # Traverse and reverse the pointers
        while True:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
            if curr == head:
                break

        # Adjust the circular connection
        head.next = prev
        head = prev

        return head

                
        

        


#{ 
 # Driver Code Starts
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


def printList(head):
    if head is None:
        print("empty")
        return

    temp = head
    while True:
        print(temp.data, end=" ")
        temp = temp.next
        if temp == head:
            break
    print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        key = int(input())

        head = Node(arr[0])
        tail = head
        for i in range(1, len(arr)):
            tail.next = Node(arr[i])
            tail = tail.next
        tail.next = head  # Make the list circular

        ob = Solution()
        head = ob.deleteNode(head, key)
        head = ob.reverse(head)
        printList(head)

# } Driver Code Ends