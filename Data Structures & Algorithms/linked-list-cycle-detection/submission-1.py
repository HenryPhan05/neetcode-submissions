# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # used two pointers , one slow and fast as second hint
        p1, p2 = head,head
        # if pointer 2 and next are not null --> loop
        while p2 and p2.next:
            #ex[1,2,3,4]            
            p1 = p1.next # p1 = 2
            p2 = p2.next.next # p2 = 3
            if p1 == p2: # 2!=3 --> looping
            #cuz index = 1, so after one loop p2 =3--> p2.next.next == 2, not =1
            # p1 and p2 will meet at third loop 
                return True
        return False

            

        
        