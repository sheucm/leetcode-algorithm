# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        
        _heap = []
        _idx = 0

        head = None
        curr = None

        for idx, node in enumerate(lists):
            if node:
                heapq.heappush(_heap, (node.val, _idx, node))
                _idx += 1
        
        while _heap:
            p_node = heapq.heappop(_heap)[2]

            next_node = p_node.next
            if next_node:
                heapq.heappush(_heap, (next_node.val, _idx, next_node))
                _idx += 1
            
            if not head:
                head = p_node
            if not curr:
                curr = p_node
            else:
                curr.next = p_node
                curr = curr.next
            curr.next = None
        return head
            
            


        
