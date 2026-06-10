# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        prev_node = head 
        current_node = head.next if head else None
        
        while current_node:
            if current_node.val == prev_node.val:
                prev_node.next = current_node.next 
                    
            else:
                prev_node = current_node

            current_node = current_node.next
        return head
        
        