# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """

        slow = head
        fast = head 

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        current = slow

        while current:
            next_node = current.next 
            current.next = prev
            prev = current
            current = next_node
        

        while head and prev:
            current_head = head
            current_prev = prev

            if current_head.val != current_prev.val:
                return False
            
            head = head.next
            prev = prev.next

        return True
