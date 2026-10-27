# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # return no value
        if not head:
            return 
        # initialize array
        nodes = []
        # current = head
        cur = head
        # append into nodes
        while cur: 
            nodes.append(cur)
            cur = cur.next
        # using two pointers 
        i, j = 0 , len(nodes) -1
        # loop 
        while i< j:
            # set next node equal last node
            nodes[i].next = nodes[j]
            # move to the next node
            i+=1
            #set the stop when two pointers meet up
            if i >=j:
                break
            #next node is node[i]
            nodes[j].next = nodes[i]
            # reduce the node position 
            j-=1
        #after loop, tail is None
        nodes[i].next = None



        
        
        
        
        

        