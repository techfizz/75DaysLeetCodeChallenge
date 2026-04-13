# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = head
        slow = head
        
        # Move fast pointer n steps ahead
        for _ in range(n):
            fast = fast.next
        
        # If fast is None → remove head
        if not fast:
            return head.next
        
        # Move both pointers until fast reaches last node
        while fast.next:
            fast = fast.next
            slow = slow.next
        
        # Delete the nth node from end
        slow.next = slow.next.next
        
        return head
        