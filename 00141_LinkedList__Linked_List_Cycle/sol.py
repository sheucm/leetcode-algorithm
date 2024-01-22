# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from collections import defaultdict
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        ### Solution: Use slow and fast variable
        ### Time Complexity: O(N)
        ### Time Complexity: O(1)
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False


        ### Solution: Hash Map
        ### Time Complexity: O(N)
        ### Time Complexity: O(N)
        # vis = defaultdict(bool)
        # while head:
        #     if vis[head]:
        #         return True
        #     vis[head] = True
        #     head = head.next
        # return False