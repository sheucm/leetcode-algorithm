# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        ### Solution1: Iterative
        ### Time Complexity: O(N)
        ### Space Complexity: O(1)
        prev, curr = None, head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev


        ### Solution2: Recursive
        ### Time Complexity: O(N)
        ### Space Complexity: O(1)
        # if not head or not head.next:
        #     return head
        # new_head = self.reverseList(head.next)
        # head.next.next = head
        # head.next = None
        # return new_head



