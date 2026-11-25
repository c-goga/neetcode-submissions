# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, n = None, None
        while head != None:
            n = head.next
            # print('n', n.val)
            head.next = prev
            # if prev != None:
                # print('head.next', head.next.val)
            prev = head
            # print('prev', prev.val)
            head = n
            # print('head', head.val)
        
        return prev
            
        