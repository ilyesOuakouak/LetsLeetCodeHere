# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        slow = head
        fast = head
        meeting_occured = False
        meetting_pointer = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if fast == slow:
                meeting_occured = True
                break
        
        if meeting_occured:
            while slow != meetting_pointer:
                meetting_pointer = meetting_pointer.next
                slow = slow.next
            
            return slow


        return None
            
