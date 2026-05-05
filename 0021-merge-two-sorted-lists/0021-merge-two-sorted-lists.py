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
    

"""
    dummy = ListNode(-1)
    current = dummy

    while list1 and list2:
        if list1.val < list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next

    
    current.next = list1 if list1 else list2
    
    # this line is just saying this 
    # Is list1 NOT empty?
    if list1:
        current.next = list1  # Hook the ENTIRE remaining chain of list1 here.
    # Otherwise (if list1 is empty), it must be list2 that has stuff left.
    else:
        current.next = list2  # Hook the ENTIRE remaining chain of list2 here.
    

    return dummy.next

 """

"""
    State:  [Dummy] -> [Node A]
                ^
            current is here

    Action: current.next = Node B
            current = current.next
    Result: [Dummy] -> [Node A] -> [Node B]
                            ^
                        current is here!

    Action: current = current.next
    Result: [Dummy] -> [Node A] -> [Node B]
                                        ^
                                    Current is NOW here. Ready for Node C.
"""