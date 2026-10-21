# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #if list 1  == [] --> list2 --> dont need sorted
        if not list1: 
            return list2
        #otherwise dont need sorted list1
        elif not list2:
            return list1
        # all emptied --> []
        elif not list1 and not list2:
            return None
        else:
            #compare current list 1 and current list 2
            if list1.val <= list2.val: # cur list 1 less or equal than cur list 2
                # recursion to compare next list 1 and cur list 2
                list1.next = self.mergeTwoLists(list1.next, list2)
                return list1 # compare then return the number less than the other one
            else: 
                # if list2.cur greater than list1.val
                #recursion to compare next list2 and cur list 1
                list2.next = self.mergeTwoLists(list1, list2.next)
                return list2 # return the number less than the other one
            
                
              
        