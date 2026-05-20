# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Step 1: Create a dummy node to anchor the start of the merged list
        dummy = ListNode()
        tail = dummy
        
        # Step 2: Zipper the lists together while both have nodes
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
                
            tail = tail.next
            
        # Step 3: Attach any remaining nodes from either list
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2
            
        # Step 4: Return the head of the newly merged list (skipping the dummy)
        return dummy.next