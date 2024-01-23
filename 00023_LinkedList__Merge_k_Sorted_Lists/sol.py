# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:

    def _merge(self, li1, li2):
        """
        The solution of "21. Merge Two Sorted Lists"
        """
        dummy = ListNode()
        tail = dummy
        while li1 and li2:
            if li1.val <= li2.val:
                tail.next = li1
                li1 = li1.next
            else:
                tail.next = li2
                li2 = li2.next
            tail = tail.next
        tail.next = None
        if li1:
            tail.next = li1
        elif li2:
            tail.next = li2
        return dummy.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        ### Solution 1: Merge Sort
        ### Time Complexity: O(N * logK)
        ### Space Complexity: O(N*K)
        if not lists:
            return None
        while len(lists) > 1:
            m_li = []
            for i in range(0, len(lists), 2):
                li1 = lists[i]
                li2 = lists[i+1] if (i+1) < len(lists) else None
                m_li.append(self._merge(li1, li2))
            lists = m_li
        return lists[0]


        ### Solution2: Heap
        ### Time Complexity: O(N * logK)
        ### Space Complexity: O(N*K)
        # if not lists: return None
        # h = []
        # for idx, li in enumerate(lists):
        #     if not li: continue
        #     heapq.heappush(h, (li.val, idx, li))
        # dummy = ListNode()
        # tail = dummy
        # while h:
        #     val, idx, node = heapq.heappop(h)
        #     lists[idx] = lists[idx].next
        #     if lists[idx]:
        #         heapq.heappush(h, (lists[idx].val, idx, lists[idx]))
        #     tail.next = node
        #     tail = tail.next
        # tail.next = None
        # return dummy.next
            
            
