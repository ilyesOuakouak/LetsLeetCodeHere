# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        
        dummy = ListNode()
        currentNode = dummy

        while list1 and list2:
            if list1.val < list2.val:
                currentNode.next = list1
                list1 = list1.next
                currentNode = currentNode.next 
            else:
                currentNode.next = list2
                list2 = list2.next
                currentNode = currentNode.next

            
        currentNode.next = list1 or list2

        return dummy.next